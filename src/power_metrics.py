import os
import subprocess
import parser
from datetime import datetime

from src.file_management import FileManagement


class Powermetrics:
    def generate_output_file_name(base_name):
        count = 1
        file_name = f"{base_name}{count}.txt"
        while os.path.exists(file_name):
            file_name = f"{base_name}{count}.txt"
            count += 1
        return file_name

    @staticmethod
    def gather_data(number_of_samples, sampling_interval, password, output_file_path):
        output_path_powermetrics= output_file_path + "_powermetrics"
        file_manager = FileManagement()
        output_path_powermetrics = file_manager.generate_output_file_name(output_path_powermetrics)
        datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        sudo_command = f"sudo -S powermetrics -i {sampling_interval} -n {number_of_samples} --show-process-energy | grep -iE 'ffplay|ALL_TASKS|NAME'"
        print(f"{sudo_command} \n executing .....if not started please make sure the power"
              f"metrics sudo password is correct.[src/configuration.config]")
        process = subprocess.Popen(sudo_command, shell=True, stdin=subprocess.PIPE, universal_newlines=True,
                                   stdout=subprocess.PIPE, text=True)

        process.stdin.write(password+'\n')
        process.stdin.flush()

        for line in process.stdout:
            print("*************** saving powermetrics output *************** ")
            timestamp_current = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            with open(output_path_powermetrics, 'a') as file:
                if "Name" in line:
                    file.write(f"Timestamp: {timestamp_current}\n")
                file.write(line)
            print(f"Timestamp: {timestamp_current}\n{line}")
        timestamp_end = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"end-Timestamp: {timestamp_end}")

if __name__ == "__main__":
    pd = Powermetrics()
    config = parser.Parser()
    config_data = parser.Parser()
    pas = config_data.get_credentials()
    output_path = config_data.get_output_path()
    pd.gather_data(100, 2, pas, output_path+"/try.txt")
