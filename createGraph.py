import networkx as nx
import matplotlib.pyplot as plt
import random
import math
import scipy as sp

from PySpice.Spice.Netlist import Circuit
from PySpice.Unit import *



import networkx as nx
import matplotlib.pyplot as plt

m = 5000
n = math.floor(m/1.5)

net = 'testCircuit' +str(m)+'.net'
csv = 'testCircuit' +str(m)+'.csv'

G = nx.gnm_random_graph(n, m)

num_nodes = G.number_of_nodes()

for (node0, node1) in G.edges():
    G[node0][node1]['weight'] = random.randint(1, 1000)

with open(csv, 'w') as file:
    i = 1
    file.write(",,,,,,\n")
    for (node0, node1, attr) in G.edges(data=True):
        identifier = "C"+str(i)
        i+=1
        capacitance = attr['weight']
        if(capacitance>1000):
            capacitance /= 1000
            unit = "p"
        else:
            unit = "f"
        file.write(f",,{identifier},{node0},{node1},{capacitance},{unit}\n")

with open(net, 'w') as file:
    i = 1
    for (node0, node1, attr) in G.edges(data=True):
        identifier = "C"+str(i)
        i+=1
        capacitance = attr['weight']
        if(capacitance>1000):
            capacitance /= 1000
            unit = "p"
        else:
            unit = "f"
        file.write(f"{identifier} {node0} {node1} {capacitance} {unit}\n")

    


# G = nx.Graph()

# n = 50



# G.add_nodes_from(range(n))

# for node in G.nodes():
#     connections = random.randint(1, 3) 
#     possible_targets = list(set(G.nodes()) - {node})  
#     for _ in range(connections):
#         if not possible_targets: 
#             break
#         target = random.choice(possible_targets)
#         weight = random.randint(0, 1000)  
#         G.add_edge(node, target, weight=weight)
#         possible_targets.remove(target) 


# plt.figure(figsize=(12, 8))
# pos = nx.kamada_kawai_layout(G)
# print(nx.is_connected(G))

# nx.draw_networkx_nodes(G, pos, node_size=20)

# edges = G.edges(data=True)
# nx.draw_networkx_edges(G, pos, edgelist=edges, edge_color="gray")

# edge_labels = dict([((u, v,), d['weight'])
#                     for u, v, d in G.edges(data=True)])
# nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=7)

# plt.title("Random Network")
# plt.axis('off')  
# plt.show()

