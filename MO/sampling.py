import argparse
import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt
from gerrychain.random import random
random.seed(20210511)
from gerrychain import Graph, Partition, Election, MarkovChain, GeographicPartition, accept, constraints
from gerrychain.updaters import Tally, cut_edges
from gerrychain.constraints import single_flip_contiguous, Validator, within_percent_of_ideal_population, refuse_new_splits
from gerrychain.proposals import recom
from gerrychain.accept import always_accept
from gerrychain.tree import recursive_tree_part
import numpy as np 
from functools import partial
import json
import csv
import pickle

# save np.load
np_load_old = np.load

# modify the default parameters of np.load
np.load = lambda *a,**k: np_load_old(*a, allow_pickle=True, **k)

## ## ## ## ## ## ## ## ## ## ## 
## set-up argparse!
## ## ## ## ## ## ## ## ## ## ##

parser = argparse.ArgumentParser(description="MO ensemble", 
                                 prog="sampling.py")
parser.add_argument("map", metavar="map", type=str,
                    choices=["state_house", "state_senate"],
                    help="the map to redistrict")
parser.add_argument("eps", metavar="epsilon", type=float,
                    # choices=[0.01, 0.03, 0.05, .08],
                    help="population deviation across districts")
parser.add_argument("n", metavar="iterations", type=int,
                    help="the number of plans to sample")
args = parser.parse_args()

num_districts_in_map = {"state_senate" : 34,
                        "state_house" : 163}

POP_COL = "POP10"
NUM_DISTRICTS = num_districts_in_map[args.map]
ITERS = args.n
EPS = args.eps
ELECTS = ["PRES16", "USSEN16"]

## ## ## ## ## ## ## ## ## ## ## 
## creating an initial partition
## ## ## ## ## ## ## ## ## ## ## 
print("Reading in Data/Graph")

dat_path = "/Users/hopecj/projects/gerryspam/MO/dat/final_prec/prec_labeled.shp"
dat = gpd.read_file(dat_path)
list(dat.columns)
dat['SLDUST'].nunique()
dat['SLDLST'].nunique()

elections = [Election("USSEN16", {"Dem": "G16USSDKAN", "Rep": "G16USSRBLU"}),
             Election("PRES16", {"Dem": "G16PREDCLI", "Rep": "G16PRERTRU"})]

graph = Graph.from_file(dat_path)

mo_updaters = {"population" : Tally(POP_COL, alias="population"),
               "cut_edges": cut_edges,
            }

election_updaters = {election.name: election for election in elections}
mo_updaters.update(election_updaters)

## ## ## ## ## ## ## ## ## ## ## 
## Initial partition
## ## ## ## ## ## ## ## ## ## ## 

print("Creating seed plan")

# assignment of the nodes of the graph into parts of the partition
# this is where we need to tell the Partiion to assign nodes by their 
# "SLDUST" or "SLDLST" attribute in the shapefile

##################################################################
######## ! if using a random map as the initial partition
##################################################################
# NUM_DISTRICTS=34
# EPS=0.05
# total_pop = sum(dat[POP_COL])
# ideal_pop = total_pop / NUM_DISTRICTS
# cddict = recursive_tree_part(graph=graph, parts=range(NUM_DISTRICTS), 
#                                 pop_target=ideal_pop, pop_col=POP_COL, epsilon=EPS)

# init_partition = Partition(graph, assignment=cddict, updaters=mo_updaters)
# init_partition["USSEN16"].efficiency_gap() #PRES EG = -0.08, USSEN EG = -0.18


##################################################################
######## ! if using the ~0 EG map as the initial partition
##################################################################
# init_partition = GeographicPartition(graph, assignment="SLDUST", updaters=mo_updaters)
# # init_partition["USSEN16"].efficiency_gap() #PRES EG = -0.04, USSEN EG = -0.15
sen_parts = np.load("/Users/hopecj/projects/gerryspam/MO/res_0527/MO_state_senate_1000_0.05_parts.p")
chain_assignment = sen_parts["samples"][151] # just show the first one, change index for a different part
init_partition = Partition(graph, assignment=chain_assignment, updaters=mo_updaters)
total_pop = sum(dat[POP_COL])
ideal_pop = total_pop / NUM_DISTRICTS

# init_partition.plot(cmap="tab20")
# init_partition["USSEN16"].efficiency_gap() #PRES EG = -0.04, USSEN EG = -0.14
# plt.show()

##################################################################
######## ! if using the actual state senate map as the initial partition
##################################################################
# init_partition = GeographicPartition(graph, assignment="SLDUST", updaters=mo_updaters)
# init_partition["USSEN16"].efficiency_gap() #PRES EG = -0.04, USSEN EG = -0.15
# ideal_pop = sum(init_partition['population'].values()) / len(init_partition)

## ## ## ## ## ## ## ## ## ## ## 
## set up a chain 
## ## ## ## ## ## ## ## ## ## ## 
proposal = partial(recom, pop_col=POP_COL, pop_target=ideal_pop, epsilon=EPS, 
                   node_repeats=1)

# to do: update compactness bound here
# current one = bounding the number of cut edges at 2 times the number of cut edges from the initial plan.
compactness_bound = constraints.UpperBound(lambda p: len(p["cut_edges"]), 
                                           2*len(init_partition["cut_edges"]))

### if doing a one-off chain 
# chain = MarkovChain(
#     proposal=proposal,
#     constraints=[
#             constraints.within_percent_of_ideal_population(init_partition, 0.055),
#         compactness_bound
#     ],
#     accept=accept.always_accept,
#     initial_state=init_partition,
#     total_steps=100000
# )

# def make_dat_from_chain(chain, id):
#     d_percents = [partition["PRES16"].percents("Dem") for partition in chain]
#     ensemble_dat = pd.DataFrame(d_percents)
#     ensemble_dat["id"] = id
#     egs = [partition["PRES16"].efficiency_gap() for partition in chain]
#     ensemble_dat["eg"] = egs
#     mm = [partition["PRES16"].mean_median() for partition in chain]
#     ensemble_dat["mm"] = mm
#     seats = [partition["PRES16"].seats("Dem") for partition in chain]
#     ensemble_dat["D_seats"] = seats
#     return ensemble_dat

# # start 12:38 - took ~6 hours
# dat1 = make_dat_from_chain(chain, "st_sen_5.5eps_enactedinit") # took abt 4 hours
# dat1.to_csv("/Users/hopecj/projects/gerryspam/MO/res/st_sen_5_5eps_enactedinit.csv")
# small_dat1 = dat1.sample(1000) # randomly sample 1000 rows
# small_dat1.to_csv("/Users/hopecj/projects/gerryspam/MO/res/st_sen_5_5eps_enactedinit_sampled.csv")
# plt.hist(dat1["eg"], bins=50)
# plt.show()


## ## ## ## ## ## ## ## ## ## ## 
## Re-com chain and run it!
## ## ## ## ## ## ## ## ## ## ## 
chain = MarkovChain(
        proposal,
        constraints=[
            constraints.within_percent_of_ideal_population(init_partition, EPS),
            compactness_bound],
        accept=accept.always_accept,
        initial_state=init_partition,
        total_steps=ITERS)

print("Starting Markov Chain")

def init_chain_results(elections):
    data = {"cutedges": np.zeros(ITERS)}
    parts = {"hash": [], "samples": [], "eg": [], "election": []}

    for election in elections:
        name = election.lower()
        data["seats_{}".format(name)] = np.zeros(ITERS)
        data["results_{}".format(name)] = np.zeros((ITERS, NUM_DISTRICTS))
        data["efficiency_gap_{}".format(name)] = np.zeros(ITERS)
        data["mean_median_{}".format(name)] = np.zeros(ITERS)
        data["partisan_gini_{}".format(name)] = np.zeros(ITERS)
    return data, parts

def tract_chain_results(data, elections, part, i):
    data["cutedges"][i] = len(part["cut_edges"])

    for election in elections:
        name = election.lower()
        data["results_{}".format(name)][i] = sorted(part[election].percents("Dem"))
        data["seats_{}".format(name)][i] = part[election].seats("Dem")
        data["efficiency_gap_{}".format(name)][i] = part[election].efficiency_gap()
        data["mean_median_{}".format(name)][i] = part[election].mean_median()
        data["partisan_gini_{}".format(name)][i] = part[election].partisan_gini()

def update_saved_parts(parts, part, elections, i):
    # if i % (ITERS / 10) == 99: parts["samples"].append(part.assignment)
    for election in elections: 
        # save any plan with netural or outlier EG 
        if (part[election].efficiency_gap() < -.15): parts["samples"].append(part.assignment)
        if (part[election].efficiency_gap() > .15): parts["samples"].append(part.assignment)
        if (part[election].efficiency_gap() > -.03) and (part[election].efficiency_gap() < .03): parts["samples"].append(part.assignment)
        if (part[election].efficiency_gap() < -.15): 
            parts["eg"].append(part[election].efficiency_gap())
            parts["election"].append(election)
            parts["hash"].append(i)
        if (part[election].efficiency_gap() > .15): 
            parts["eg"].append(part[election].efficiency_gap())
            parts["election"].append(election)
            parts["hash"].append(i)
        if (part[election].efficiency_gap() > -.03) and (part[election].efficiency_gap() < .03): 
            parts["eg"].append(part[election].efficiency_gap())
            parts["election"].append(election)
            parts["hash"].append(i)

chain_results, parts = init_chain_results(ELECTS)

for i, part in enumerate(chain):
    chain_results["cutedges"][i] = len(part["cut_edges"])
    tract_chain_results(chain_results, ELECTS, part, i)
    update_saved_parts(parts, part, ELECTS, i)

    if i % 1000 == 0:
        print("*", end="", flush=True)
print()

## ## ## ## ## ## ## ## ## ## ## 
## Save it 
## ## ## ## ## ## ## ## ## ## ## 

print("Saving results")

dat_path = "/Users/hopecj/projects/gerryspam/MO/dat/final_prec/prec_labeled.shp"

output = "/Users/hopecj/projects/gerryspam/MO/res_0528/MO_{}_{}_{}.p".format(args.map, ITERS, EPS)
output_parts = "/Users/hopecj/projects/gerryspam/MO/res_0528/MO_{}_{}_{}_parts.p".format(args.map, ITERS, EPS)

with open(output, "wb") as f_out:
    pickle.dump(chain_results, f_out)

with open(output_parts, "wb") as f_out:
    pickle.dump(parts, f_out)
