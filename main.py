from src import power_metrics
from src import parser
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    config_parser= parser.Parser()
    pas = config_parser.get_credentials()
    output = config_parser.get_output_path()
    print(pas)
    pd = power_metrics.powermetrics()
    # calculate number of samples and interval to be
    pd.gather_data(100, 20, pas,output)
