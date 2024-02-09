import re
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

#     Extracts the frames per second (fps) from a log file.
def extract_fps(log_file_path):
    with open(log_file_path, 'r') as file:
        log_data = file.read()
    match = re.search(r"(\d+)\s*fps", log_data)
    if match:
        return int(match.group(1))
    else:
        return None

#     Calculates the average brightness per second from a brightness data file.
def calculate_average_brightness(brightness_file_path, fps):

    with open(brightness_file_path, 'r') as file:
        file.readline()  # Skip the first line
        start_timestamp_line = file.readline().strip()  # Extract timestamp from the second line
        start_timestamp_str = re.search(r"start-Timestamp: (.+)", start_timestamp_line).group(1)
        start_timestamp = datetime.strptime(start_timestamp_str, "%Y-%m-%d %H:%M:%S")
        brightness_data = eval(file.readline())  # Extract the array from the third line
    brightness_per_second = [sum(brightness_data[i:i + fps]) / fps for i in range(0, len(brightness_data), fps)]
    return brightness_per_second, start_timestamp

#     Extracts and calculates the energy consumption percentage of ffplay compared to ALL_TASKS from a powermetrics data file.
def extract_and_calculate_percentage(powermetrics_file_path, start_timestamp):
    with open(powermetrics_file_path, 'r') as file:
        lines = file.readlines()

    energy_data = []
    for i in range(len(lines)):
        if 'Timestamp:' in lines[i]:
            if 'ffplay' in lines[i + 2] and 'ALL_TASKS' in lines[i + 3]:
                timestamp_str = lines[i].split('Timestamp: ')[1].strip()
                current_timestamp = datetime.strptime(timestamp_str, "%Y-%m-%d %H:%M:%S")
                if current_timestamp >= start_timestamp:
                    ffplay_energy_impact_match = re.search(r"ffplay\s+.*\s+(\d+\.\d+)\s*$", lines[i + 2])
                    ffplay_energy_impact = float(ffplay_energy_impact_match.group(1)) if ffplay_energy_impact_match else 0

                    all_tasks_energy_impact_match = re.search(r"ALL_TASKS\s+.*\s+(\d+\.\d+)\s*$", lines[i + 3])
                    all_tasks_energy_impact = float(all_tasks_energy_impact_match.group(1)) if all_tasks_energy_impact_match else 0
                    percentage = (ffplay_energy_impact / all_tasks_energy_impact * 100) if all_tasks_energy_impact != 0 else 0
                    energy_data.append({'timestamp': current_timestamp, 'percentage': percentage})

    # Group data by second and calculate the average percentage
    energy_data_grouped_by_second = {}
    for entry in energy_data:
        rounded_timestamp = entry['timestamp'].replace(microsecond=0)
        if rounded_timestamp not in energy_data_grouped_by_second:
            energy_data_grouped_by_second[rounded_timestamp] = []
        energy_data_grouped_by_second[rounded_timestamp].append(entry['percentage'])

    average_percentage_by_second = {timestamp: sum(percentages) / len(percentages) for timestamp, percentages in energy_data_grouped_by_second.items()}

    return average_percentage_by_second

#     Maps the brightness values to the corresponding energy consumption percentages.
def map_brightness_to_percentage(brightness_values, percentage_values):

    data_pairs = []

    start_second = list(percentage_values.keys())[0].second

    for timestamp, percentage in percentage_values.items():
        index = timestamp.second - start_second
        if index < len(brightness_values):
            brightness = brightness_values[index]
            data_pairs.append((brightness, percentage))

    return data_pairs

#     Plots a scatter diagram using mapped data pairs of brightness values and energy consumption percentages.
def plot_scatter(mapped_data_pairs, title="Brightness vs. Percentage", xlabel="Average Brightness", ylabel="ffplay Energy Consumption Percentage of ALL_TASKS"):
    x_data, y_data = zip(*mapped_data_pairs)

    plt.figure(figsize=(10, 6))
    plt.scatter(x_data, y_data, color='blue')
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.grid(True)
    plt.show()

# File paths
log_file_path = "temp_data/random_HD_25fps_10Mbps_H265_player_logs.txt"
brightness_file_path = "temp_data/random_HD_25fps_10Mbps_H265_brightness.txt"
powermetrics_file_path = "temp_data/random_HD_25fps_10Mbps_H265_powermetrics.txt"

# Extract FPS from log file
fps = extract_fps(log_file_path)

# Calculate average brightness and extract start timestamp
average_brightness_per_second, start_timestamp = calculate_average_brightness(brightness_file_path, fps)

# Extract and calculate energy consumption percentage
energy_data = extract_and_calculate_percentage(powermetrics_file_path, start_timestamp)
mapped_data_pairs = map_brightness_to_percentage(average_brightness_per_second, energy_data)
plot_scatter(mapped_data_pairs)