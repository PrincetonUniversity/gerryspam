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

## ## ## ## ## ## ## ## ## ## ## 
## set-up argparse!
## ## ## ## ## ## ## ## ## ## ##

parser = argparse.ArgumentParser(description="MO ensemble", 
                                 prog="sampling.py")
parser.add_argument("map", metavar="map", type=str,
                    choices=["state_house", "state_senate"],
                    help="the map to redistrict")
parser.add_argument("eps", metavar="epsilon", type=float,
                    choices=[0.01, 0.03, 0.05, .08],
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
            #    "VAP": Tally("VAP"),
            #    "WVAP": Tally("WVAP"),
            #    "HVAP": Tally("HVAP"),
            #    "BVAP": Tally("BVAP"),
            #    "HVAP_perc": lambda p: {k: (v / p["VAP"][k]) for k, v in p["HVAP"].items()},
            #    "WVAP_perc": lambda p: {k: (v / p["VAP"][k]) for k, v in p["WVAP"].items()},
            #    "BVAP_perc": lambda p: {k: (v / p["VAP"][k]) for k, v in p["BVAP"].items()},
            #    "BHVAP_perc": lambda p: {k: ((p["HVAP"][k] + p["BVAP"][k]) / v) for k, v in p["VAP"].items()},
            }

election_updaters = {election.name: election for election in elections}
mo_updaters.update(election_updaters)

## ## ## ## ## ## ## ## ## ## ## 
## Initial partition
## ## ## ## ## ## ## ## ## ## ## 

print("Creating seed plan")

total_pop = sum(dat[POP_COL])
ideal_pop = total_pop / NUM_DISTRICTS

# if args.map != "state_house":
cddict = recursive_tree_part(graph=graph, parts=range(NUM_DISTRICTS), 
                                pop_target=ideal_pop, pop_col=POP_COL, epsilon=EPS)
## unclear why this is done
# else:
#     with open("GA_house_seed_part_0.05.p", "rb") as f:
#         cddict = pickle.load(f)
init_partition = Partition(graph, assignment=cddict, updaters=mo_updaters)
    
## ## ## ## ## ## ## ## ## ## ## 
## set up a chain 
## ## ## ## ## ## ## ## ## ## ## 
proposal = partial(recom, pop_col=POP_COL, pop_target=ideal_pop, epsilon=EPS, 
                   node_repeats=1)

compactness_bound = constraints.UpperBound(lambda p: len(p["cut_edges"]), 
                                           2*len(init_partition["cut_edges"]))

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
    parts = {"samples": [], "compact": []}

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
    if i % (ITERS / 10) == 99: parts["samples"].append(part.assignment)

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

output = "/Users/hopecj/projects/gerryspam/MO/res/MO_{}_{}_{}.json".format(args.map, ITERS, EPS)
output_parts = "/Users/hopecj/projects/gerryspam/MO/res/MO_{}_{}_{}_parts.json".format(args.map, ITERS, EPS)

with open(output, "w") as f_out:
    json.dump(chain_results, f_out)

with open(output_parts, "w") as f_out:
    json.dump(parts, f_out)

# quick histograms
# plt.hist(dat1["eg"], bins=50)
# plt.show()

# plt.hist(small_dat1["eg"], bins=20)
# plt.show()

