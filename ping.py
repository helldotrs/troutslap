import subprocess

# Define the command you want to run as a list
command = ["echo", "Hello, world!"]

# Run the command
process = subprocess.run(command, capture_output=True, text=True)

# Print the output
print("Command output:", process.stdout)
