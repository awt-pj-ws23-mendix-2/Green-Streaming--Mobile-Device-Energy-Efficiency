import subprocess
import parser
from datetime import datetime
class Powermetrics:
    @staticmethod
    def gather_data(number_of_samples, sampling_interval, password, output_file_path):
        output_path= output_file_path+"_powermetrics.txt"
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        sudo_command = f"sudo -S powermetrics -i {sampling_interval} -n {number_of_samples} --show-process-energy | grep -iE 'ffplay|ALL_TASKS|NAME'"
        print(sudo_command)
        process = subprocess.Popen(sudo_command, shell=True, stdin=subprocess.PIPE, universal_newlines=True,
                                   stdout=subprocess.PIPE, text=True)

        process.stdin.write(password+'\n')
        process.stdin.flush()
        # output, error = process.communicate(input=password)
        # print(output)
        for line in process.stdout:
            print("***************printing line ")
            timestamp_current = datetime.now().strftime("%Y-%m-%d %H:%M:%S:%f")[:-3]
            with open(output_path, 'a') as file:
                if "Name" in line:
                    file.write(f"Timestamp: {timestamp_current}\n")
                file.write(line)
            print(f"Timestamp: {timestamp_current}\n{line}")
        timestamp_end = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(output_path, 'a') as file:
            file.write(f"end-Timestamp: {timestamp_end}\n")

        print(f"end-Timestamp: {timestamp_end}")
if __name__ == "__main__":
    pd = Powermetrics()
    config = parser.Parser()
    config_data = parser.Parser()
    pas = config_data.get_credentials()
    output_path = config_data.get_output_path()
    pd.gather_data(100, 2, pas, output_path+"/try.txt")
