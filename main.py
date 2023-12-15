import power_metrics
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    pd = power_metrics.powermetrics()
    pd.gather_data(100, 20)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
