import networkx as nx
import matplotlib.pyplot as plt
import random
import scipy as sp

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


# nx.draw_networkx_nodes(G, pos, node_size=20)

# edges = G.edges(data=True)
# nx.draw_networkx_edges(G, pos, edgelist=edges, edge_color="gray")

# edge_labels = dict([((u, v,), d['weight'])
#                     for u, v, d in G.edges(data=True)])
# nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=7)

# plt.title("Random Network")
# plt.axis('off')  
# plt.show()




from PySpice.Spice.Netlist import Circuit
from PySpice.Unit import *

count = 50
circuit = Circuit('Sample Circuit')

for i in range(count):
    circuit.C(i, i+1, i+2, 5@u_uF)
    print(i)


# Create the circuit
circuit.SinusoidalVoltageSource('source', 1, circuit.gnd, amplitude=1@u_V, frequency=1@u_kHz)

circuit.R('esistor', 51, circuit.gnd, 1@u_MΩ)


# Export the circuit to a netlist file
netlist_filename = 'sample_circuit.cir'
with open(netlist_filename, 'w') as netlist_file:
    netlist_file.write(str(circuit))
