from gerrychain import Partition, Graph

graph = Graph()
graph.add_edges_from([(0, 1), (1, 2), (2, 0)]) # Arbitrary. copied this from Updaters documentation

POP_COL = 'vap'
VRA_POP_COL = 'bvap'

'''
Fake data here. Node 0 and 2 have enough to qualify alone, but pairing/districting
Node 1 with either can tank it.
'''

graph.nodes[0][POP_COL] = 100
graph.nodes[0][VRA_POP_COL] = 60

graph.nodes[1][POP_COL] = 100
graph.nodes[1][VRA_POP_COL] = 0

graph.nodes[2][POP_COL] = 100
graph.nodes[2][VRA_POP_COL] = 40

def num_vra_districts(partition, pop_col=POP_COL, vra_pop_col=VRA_POP_COL, vra_relative_threshold=0.37):
    # we'll count districts that satisfy the VRA threshold.
    total = 0

    # For each district,...
    for district in partition.parts:
        nodes = partition.parts[district]

        # compute total population...
        pop = sum(partition.graph.nodes[n][pop_col] for n in nodes)

        # and VRA-relevant population...
        vra_pop = sum(partition.graph.nodes[n][vra_pop_col] for n in nodes)

        # to see if their ratio is greater than the threshold.
        if vra_pop / pop > vra_relative_threshold:
            total += 1

    return total

# This assignment (2nd argument) has all nodes in their own districts.
partition = Partition(graph, {0:0, 1:1, 2:2}, {"num_vra_districts": num_vra_districts})
assert partition.num_vra_districts == 2

# This assignment (2nd argument) has Nodes 0 and 1 in the same district, 2 alone.
partition = Partition(graph, {0:0, 1:0, 2:1}, {"num_vra_districts": num_vra_districts})
assert partition.num_vra_districts == 1

