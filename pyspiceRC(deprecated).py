import matplotlib.pyplot as plt
from PySpice.Probe.Plot import plot
from PySpice.Spice.Netlist import Circuit
from PySpice.Unit import *

# Create the circuit
circuit = Circuit('Capacitor Resistor Circuit')

# add components 
circuit.SinusoidalVoltageSource(1, 'input', circuit.gnd, amplitude=1@u_V, frequency=1@u_kHz)
circuit.C('C', 'input', 'C2', 1@u_uF)
circuit.R('R', 'C2', circuit.gnd, 1@u_kOhm)

# run the simulation 
simulator = circuit.simulator(temperature=25, nominal_temperature=25)
analysis = simulator.transient(step_time=1@u_us, end_time=10@u_ms)

# set up the plot
time = analysis.time
voltage = analysis['C2']  

plt.plot(time, voltage)
plt.grid(True)
plt.title('AC Analysis')
plt.xlabel('Frequency [Hz]')
plt.ylabel('Voltage [V]')
plt.show()



from PySpice.Spice.Netlist import Circuit
from PySpice.Unit import *

# Create the circuit
circuit = Circuit('Sample Circuit')
circuit.V('1', 'input', circuit.gnd, 'DC 5V')
circuit.R('1', 'input', 'output', 1@u_kΩ)
circuit.C('1', 'output', circuit.gnd, 100@u_nF)

# Export the circuit to a netlist file
netlist_filename = 'sample_circuit.cir'
with open(netlist_filename, 'w') as netlist_file:
    netlist_file.write(str(circuit))
