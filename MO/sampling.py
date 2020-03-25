import geopandas as gpd
from gerrychain import Graph, Partition, Election
from gerrychain.updaters import Tally, cut_edges

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