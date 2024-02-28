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

    custom_order = ['Lumafilter_1920x1080_H264_30secsteps_25_5000', 'Lumafilter_1920x1080_H264_30secsteps_60_5000','Lumafilter_1920x1080_H264_30secsteps_120_5000']
    ordered_dataset_names = [name for name in custom_order if name in dataset_names]
    ordered_dataset_averages = [dataset_averages[dataset_names.index(name)] for name in ordered_dataset_names]

    x_labels = ["fps "+name.split('_')[4] for name in ordered_dataset_names]


    bars = plt.bar(x_labels, ordered_dataset_averages)

    # bars = plt.bar(dataset_names, dataset_averages)
    plt.ylabel('Percentage of Energy Consumption')
    plt.title('Comparison of energy consumption with different fps')

    for bar in bars:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width() / 2.0, height, f'{height:.2f}', ha='center', va='bottom')

    plt.savefig('graph/dataset_comparison_fps.png')
    plt.show()


def get_dataset_groups(directory):
    dataset_groups = defaultdict(list)
    for file in os.listdir(directory):
        if file.endswith('.csv'):
            base_name = file.rsplit('.', 1)[0]
            dataset_name = base_name.rsplit('_', 1)[0]
            print(dataset_name)
            dataset_groups[dataset_name].append(os.path.join(directory, file))
    return dataset_groups


directory = 'csv_output'

dataset_groups = get_dataset_groups(directory)

plot_dataset_comparisons(dataset_groups)
