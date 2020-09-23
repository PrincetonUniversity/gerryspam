from gerrychain import Partition, Graph
import math
from gerrychain.metrics.compactness import compute_polsby_popper, polsby_popper
from gerrychain.updaters import (
    Tally,
    boundary_nodes,
    cut_edges,
    cut_edges_by_part,
    exterior_boundaries,
    interior_boundaries,
    perimeter,
)
from gerrychain.partition.geographic import GeographicPartition

graph = Graph()
graph.add_edges_from([(0, 1), (1, 2), (2, 0)]) 

AREA_COL = 'area'
PERIM_COL = 'perimeter'

graph.nodes[0][AREA_COL] = 40   
graph.nodes[0][PERIM_COL] = 18

graph.nodes[0][AREA_COL] = 120
graph.nodes[0][PERIM_COL] = 120

graph.nodes[0][AREA_COL] = 30
graph.nodes[0][PERIM_COL] = 20

partition = GeographicPartition(graph, {0:0, 1:0, 2:2}, {"area": Tally("area", alias="area"), "polsby_popper": polsby_popper})

partition = GeographicPartition(graph, {0:0, 1:0, 2:2}, {"polsby_popper": polsby_popper})
for district, polsby_popper in partition["polsby_popper"].items():
    print("District {}: {}".format(district, polsby_popper))

MLB_team = {
     'Colorado' : 30,
     'Boston'   : 11,
     'Minnesota': 2,
     'Milwaukee': 23,
     'Seattle'  : 3}
type(MLB_team)
dict_values = MLB_team.values()
type(dict_values)
sorted_dict = sorted(MLB_team)
type(sorted_dict)

sorted_values = list(MLB_team.values())

