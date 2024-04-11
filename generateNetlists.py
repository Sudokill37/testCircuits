import networkx as nx
import matplotlib.pyplot as plt
import random
import scipy as sp

from PySpice.Spice.Netlist import Circuit
from PySpice.Unit import *

count = 50
circuit = Circuit('Sample Circuit')

for i in range(count):
    circuit.C(i, i+1, i+2, 5@u_fF)
    print(i)


# Create the circuit
circuit.SinusoidalVoltageSource('source', 1, circuit.gnd, amplitude=1@u_V, frequency=1@u_kHz)

circuit.R('esistor', 51, circuit.gnd, 1@u_MΩ)


# Export the circuit to a netlist file
netlist_filename = 'sample_circuit.cir'
with open(netlist_filename, 'w') as netlist_file:
    netlist_file.write(str(circuit))
