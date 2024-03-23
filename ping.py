import subprocess

# define
command = ["ping", "-c", "1", "127.0.0.1"]

# run
process = subprocess.run(command, capture_output=True, text=True)

# saving output
ping_output = process.stdout

print("Ping output:", ping_output)
