import subprocess
import time

netlist_file = 'sample_circuit.cir'

start_time = time.time()
result = subprocess.run(['ngspice', '-b', netlist_file], capture_output=True, text=True)
end_time = time.time()


runtime = end_time - start_time


print(result.stdout)
print(f"Simulation runtime: {runtime} seconds")


if result.stderr:
    print("Errors:", result.stderr)
