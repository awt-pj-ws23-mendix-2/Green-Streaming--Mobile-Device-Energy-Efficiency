import subprocess
import parser


class powermetrics:
    # ! DO all when the sub process has been integrated all together
    # TODO: filter the remainig form for energy impact
    # TODO: save it in a file
    # TODO: Execute multi processing or async calls to the data

    @staticmethod
    def gather_data(number_of_samples, interval):
        config_data = parser.Parser()
        sudo_command = f"sudo -S powermetrics -i {number_of_samples} -n {interval} --show-process-energy | grep -iE 'ffplay|ALL_TASKS|NAME'"
        print(sudo_command)
        # output = subprocess.check_output(sudo_command, shell=True, universal_newlines=True ,input='2252')
        output = subprocess.run(sudo_command, shell=True, universal_newlines=True, input=config_data.get_credentials(),
                                stdout=subprocess.PIPE, text=True)
        output = output.stdout
        print(output)
        with open(config_data.get_output_path(), 'w') as file:
            file.write(output)
        # filter='awk {printf "%s ", $NF}'
        # output = subprocess.check_output(filter, shell=True, universal_newlines=True)
        # print("new output")
        # print(output)


if __name__ == "__main__":
    pd = powermetrics()
    pd.gather_data(100, 20)
