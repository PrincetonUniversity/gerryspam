import geopandas as gpd
from gerrychain import Graph, Partition, Election
from gerrychain.updaters import Tally, cut_edges

prec_path = "/Users/hopecj/projects/gerryspam/MO/dat/mo_prec_labeled/mo_prec_labeled.shp"
prec = gpd.read_file(prec_path)

# STOPPED HERE 
graph = Graph.from_json("./PA_VTDs.json")

election = Election("SEN12", {"Dem": "USS12D", "Rep": "USS12R"})

initial_partition = Partition(
    graph,
    assignment="CD_2011",
    updaters={
        "cut_edges": cut_edges,
        "population": Tally("TOTPOP", alias="population"),
        "SEN12": election
    }
)