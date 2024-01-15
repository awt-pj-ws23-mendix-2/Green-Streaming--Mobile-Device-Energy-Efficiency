import subprocess
import parser
from datetime import datetime
class powermetrics:
    # ! DO all when the sub process has been integrated all together
    @staticmethod
    def gather_data(number_of_samples, sampling_interval, password, output_file_path):
        output_path= output_file_path+"_powermetrics.txt"
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        sudo_command = f"sudo -S powermetrics -i {sampling_interval} -n {number_of_samples} --show-process-energy | grep -iE 'ffplay|ALL_TASKS|NAME'"
        print(sudo_command)
        # with subprocess.Popen(sudo_command, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE,
        #                       text=True) as process:
        #     output, error = process.communicate(input=password)
        #     for line in output.splitlines():
        #         timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        #         line_with_timestamp = f"{timestamp} {line}\n"
        #         print(line_with_timestamp)
        #         with open(output_file_path, 'a') as file:
        #             file.write(line_with_timestamp)
        #


            # output, error = process.communicate(input=password)
        process = subprocess.Popen(sudo_command, shell=True, stdin=subprocess.PIPE, universal_newlines=True,
                                   stdout=subprocess.PIPE, text=True)
        output, error = process.communicate(input=password)
        print(output)
        with open(output_path, 'a') as file:
            timestamp_current= datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            file.write(f"\n start-Timestamp: {timestamp}\n end-Timestamp: {timestamp_current}\n")
            print(f"\n start-Timestamp: {timestamp}\n end-Timestamp: {timestamp_current}")
            file.write(output)

if __name__ == "__main__":
    pd = powermetrics()
    config = parser.Parser()
    config_data = parser.Parser()
    pas = config_data.get_credentials()
    output_path = config_data.get_output_path()
    pd.gather_data(100, 2, pas, output_path+"/try.txt")
