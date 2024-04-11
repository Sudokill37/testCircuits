import subprocess
import time

analysis = "\nVsource 1 0 DC 0V AC 1V SIN(0V 1V 1kHz 0s 0Hz)\n.tran 10us 1ms\n.end\n.plot tran 4"

netlist_file = 'testFiles/testCircuit10.net'
tmpfile = "tempfile.net"
with open(netlist_file, 'rb') as source_file:
    with open(tmpfile, 'wb') as dest_file:
        # Read the content of the source file
        content = source_file.read()
        # Write the content to the destination file
        dest_file.write(content)

with open(tmpfile, 'a') as file:
    # Write lines to the file
    file.write(analysis)


start_time = time.time()
result = subprocess.run(['ngspice', '-b', tmpfile], capture_output=True, text=True)
end_time = time.time()


runtime = end_time - start_time


print(result.stdout)
print(f"Simulation runtime: {runtime} seconds")


if result.stderr:
    print("Errors:", result.stderr)
