import subprocess
# Define the command to run with sudo
sudo_command = f"sudo -S powermetrics -n 1 | grep 'CPU Power:' "
sudo_command_2= f"sudo -S powermetrics -i 1000 -n 2 --show-process-energy | grep -iE 'VLC|ALL_TASKS|NAME' "
sudo_command_3= f"sudo -S powermetrics -i 1000 -n 2 --show-process-energy --show-extra-power-info   "
# Run the sudo command and capture the output
output = subprocess.check_output(sudo_command_2, shell=True, universal_newlines=True)
output2 = subprocess.check_output(sudo_command_3, shell=True, universal_newlines=True)

# Print the output
print(output)
print(output2)
