import subprocess
# Define the command to run with sudo
sudo_command = f"sudo -S powermetrics -n 1 | grep 'CPU Power:' "
sudo_command_2= "sudo powermetrics -i 1000 -n 20 --samplers tasks,battery"
# Run the sudo command and capture the output
output = subprocess.check_output(sudo_command, shell=True, universal_newlines=True)

# Print the output
print(output)
