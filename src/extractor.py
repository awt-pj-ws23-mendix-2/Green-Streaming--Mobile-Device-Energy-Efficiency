import re
import csv
import os

class Extractor:
    def __init__(self):
        pass

    def extract_and_calculate_percentage(self, input_file, output_csv_file):
        with open(input_file, 'r') as file:
            content = file.readlines()

        data = []
        for i in range(len(content)):
            if 'ffplay' in content[i]:
                # Check if the next line contains 'ALL_TASKS'
                if i + 1 < len(content) and 'ALL_TASKS' in content[i + 1]:
                    ffplay_match = re.search(r"ffplay\s+.*\s+(\d+\.\d+)\s*$", content[i])
                    all_tasks_match = re.search(r"ALL_TASKS\s+.*\s+(\d+\.\d+)\s*$", content[i + 1])
                    if ffplay_match and all_tasks_match:
                        ffplay_value = float(ffplay_match.group(1))
                        all_tasks_value = float(all_tasks_match.group(1))
                        percentage = (ffplay_value / all_tasks_value) * 100 if all_tasks_value != 0 else 0
                        data.append([ffplay_value, all_tasks_value, percentage])

        with open(output_csv_file, 'w', newline='') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(['ffplay', 'ALL_TASKS', 'percentage'])
            writer.writerows(data)

    def process_video_files(self, temp_data_folder):
        for file_name in os.listdir(temp_data_folder):
            if file_name.endswith('_powermetrics.txt'):
                input_file = os.path.join(temp_data_folder, file_name)
                output_csv_file = os.path.join(temp_data_folder, file_name.replace('_powermetrics.txt', '_powermetrics.csv'))
                self.extract_and_calculate_percentage(input_file, output_csv_file)
