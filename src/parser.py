import configparser
import os

class Parser:

    def __init__(self):
        self.config = configparser.ConfigParser()
        config_path = os.path.join(os.getcwd(), "configuration.config")
        self.config.read(config_path)

    def get_output_path(self):
        path= self.config.get("Path", 'output_path')
        return path

    def get_credentials(self):
        return self.config.get("Password", 'sudo_password')

# if __name__ == "__main__":
#     print("starting")
#     pd = Parser()
#     # print(pd.get_credentials())
#     print(pd.get_output_path())