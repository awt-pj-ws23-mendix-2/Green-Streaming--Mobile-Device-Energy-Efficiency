import subprocess
import parser


class powermetrics:
    # ! DO all when the sub process has been integrated all together
    @staticmethod
    def gather_data(number_of_samples, sampling_interval, password, output_file_path):

        sudo_command = f"sudo -S powermetrics -i {sampling_interval} -n {number_of_samples} --show-process-energy | grep -iE 'ffplay|ALL_TASKS|NAME'"
        print(sudo_command)
        output = subprocess.run(sudo_command, shell=True, universal_newlines=True, input=password,
                                stdout=subprocess.PIPE, text=True)
        output = output.stdout
        print(output)
        with open(output_file_path, 'w') as file:
            file.write(output)

if __name__ == "__main__":
    pd = powermetrics()
    config = parser.Parser()
    config_data = parser.Parser()
    pas = config_data.get_credentials()
    output_path = config_data.get_output_path()
    pd.gather_data(100, 2, pas,output_path)
