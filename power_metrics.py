import subprocess

class powermetrics:
 # TODO: filter the remainig form for energy impact
 # TODO: save it in a file
 # TODO: Execute multi threading or async calls to the data

    @staticmethod
    def gather_data(number_of_samples, interval):
        sudo_command=f"sudo -S powermetrics -i {number_of_samples} -n {interval} --show-process-energy | grep -iE 'ffplay|ALL_TASKS|NAME'"
        print(sudo_command)
        # output = subprocess.check_output(sudo_command, shell=True, universal_newlines=True ,input='2252')
        output = subprocess.run(sudo_command, shell=True, universal_newlines=True ,input='2252',stdout=subprocess.PIPE, text=True)
        output = output.stdout
        print(output)
        with open('output.txt', 'w') as file:
            file.write(output)
        # filter='awk {printf "%s ", $NF}'
        # output = subprocess.check_output(filter, shell=True, universal_newlines=True)
        # print("new output")
        # print(output)
if __name__ == "__main__":
    pd = powermetrics()
    pd.gather_data(100,20)