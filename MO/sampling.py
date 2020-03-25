import geopandas as gpd
import pandas as pd
from gerrychain import Graph, Partition, Election, MarkovChain
from gerrychain.updaters import Tally, cut_edges
from gerrychain.constraints import single_flip_contiguous
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
        "population": Tally("POP10", alias="population"),
        "SEN16": election
    }
)

# total pop in each congressional district:
for district, pop in initial_partition["population"].items():
    print("District {}: {}".format(district, pop))
    
## ## ## ## ## ## ## ## ## ## ## 
## running a chain 
## ## ## ## ## ## ## ## ## ## ## 

chain = MarkovChain(
    proposal=propose_random_flip,
    constraints=[single_flip_contiguous],
    accept=always_accept,
    initial_state=initial_partition,
    total_steps=1000
)

for partition in chain:
    print(sorted(partition["SEN16"].percents("Dem")))
    
d_percents = [sorted(partition["SEN16"].percents("Dem")) for partition in chain]

ensemble_dat = pd.DataFrame(d_percents)