import pandas as pd
import matplotlib.pyplot as plt
import os
from collections import defaultdict

def calculate_average_percentage(file_path):
    data = pd.read_csv(file_path)
    return data['percentage'].mean()

def calculate_dataset_average(file_paths):
    averages = [calculate_average_percentage(file) for file in file_paths]
    return sum(averages) / len(averages)

def plot_dataset_comparisons(dataset_groups):
    dataset_names = []
    dataset_averages = []

    for dataset_name, file_paths in dataset_groups.items():
        dataset_average = calculate_dataset_average(file_paths)
        dataset_names.append(dataset_name)
        dataset_averages.append(dataset_average)

    plt.bar(dataset_names, dataset_averages)
    plt.ylabel('Average of Averages')
    plt.title('Comparison of Dataset Averages')
    plt.show()

def get_dataset_groups(directory):
    dataset_groups = defaultdict(list)
    for file in os.listdir(directory):
        if file.endswith('.csv'):
            dataset_name = file.split('_')[0]
            dataset_groups[dataset_name].append(os.path.join(directory, file))
    return dataset_groups


directory = 'temp_data'

dataset_groups = get_dataset_groups(directory)

plot_dataset_comparisons(dataset_groups)
