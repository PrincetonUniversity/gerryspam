import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt
from gerrychain import Graph, Partition, Election, MarkovChain
from gerrychain.updaters import Tally, cut_edges, election, county_splits
from gerrychain.constraints import single_flip_contiguous, Validator, within_percent_of_ideal_population, refuse_new_splits
from gerrychain.proposals import propose_random_flip
from gerrychain.accept import always_accept

## ## ## ## ## ## ## ## ## ## ## 
## creating an initial partition
## ## ## ## ## ## ## ## ## ## ## 
dat_path = "/Users/hopecj/projects/gerryspam/MO/dat/final_prec/prec_labeled.shp"
dat = gpd.read_file(dat_path)
list(dat.columns)

graph = Graph.from_file(dat_path)

election = Election("SEN16", {"Dem": "G16USSDKAN", "Rep": "G16USSRBLU"})

initial_partition = Partition(
    graph,
    assignment="CD115FP",
    updaters={
        "cut_edges": cut_edges,
        "population": Tally("POP10", alias="population"), # class gerrychain.updaters.Tally(fields, alias=None, dtype=<class ’int’>)
        "SEN16": election,
        "splits": county_splits("initial", "COUNTYFP"),
    }
)
initial_partition["SEN16"].efficiency_gap()

# total pop in each congressional district:
for district, pop in initial_partition["population"].items():
    print("District {}: {}".format(district, pop))
    
## ## ## ## ## ## ## ## ## ## ## 
## running a chain 
## ## ## ## ## ## ## ## ## ## ## 
def make_dat_from_chain(chain, id):
    d_percents = [partition["SEN16"].percents("Dem") for partition in chain]
    ensemble_dat = pd.DataFrame(d_percents)
    ensemble_dat["id"] = id
    egs = [partition["SEN16"].efficiency_gap() for partition in chain]
    ensemble_dat["eg"] = egs
    seats = [partition["SEN16"].seats("Dem") for partition in chain]
    ensemble_dat["D_seats"] = seats
    return ensemble_dat

######## chain 1: no constraints
## ## ## ## ## ## ## ## ## ## ## 
chain = MarkovChain(
    proposal=propose_random_flip, 
    constraints=[single_flip_contiguous],
    accept=always_accept,
    initial_state=initial_partition,
    total_steps=1000000              # try for a million
)

dat1 = make_dat_from_chain(chain, "single-flip-contiguous") # took abt 4 hours
dat1.to_csv("single-flip-contiguous.csv")
small_dat1 = dat1.sample(1000) # randomly sample 1000 rows
small_dat1.to_csv("single-flip-contiguous_small.csv")
# quick histograms
plt.hist(dat1["eg"], bins=50)
plt.show()

plt.hist(small_dat1["eg"], bins=20)
plt.show()

######## chain 2: constraints
## ## ## ## ## ## ## ## ## ## ## 

county_constraint = refuse_new_splits(initial_partition["splits"])
pop_constraint = within_percent_of_ideal_population(initial_partition, 0.02)

chain2 = MarkovChain(
    proposal=propose_random_flip, 
    # constraints=[county_constraint, pop_constraint],
    constraints=[pop_constraint],
    accept=always_accept, 
    initial_state=initial_partition,
    total_steps=1000000              # try for a million
)

dat2 = make_dat_from_chain(chain2, "pop-constraint") 
dat2.to_csv("pop-constraint.csv")
small_dat2 = dat2.sample(1000) # randomly sample 1000 rows
small_dat2.to_csv("pop-constrained_small.csv")

plt.hist(dat2["eg"], bins=100)
plt.show()

# add counts
# votes = [partition["SEN16"].votes("Dem") for partition in chain]
# ensemble_dat["D_votes"] = votes


