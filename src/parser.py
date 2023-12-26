import configparser


class Parser:

    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read("./src/configuration.config")

    def get_output_path(self):
        return self.config.get("Path", 'output_path')

    def get_credentials(self):
        return self.config.get("Password", 'sudo_password')
