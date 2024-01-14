import re
import os


class FileManagement:
    def __init__(self):
        pass

    def get_filename(self, path):
        match = re.search(r'([^/\\]+)\.mp4$', path)
        return match.group(1)

    def write_file(self, output, file_path):
        if os.path.exists(file_path):
            with open(file_path, 'a') as file:
                file.write(output)
            print(f"Data successfully written to {file_path}")
        else:
            print(f"Error: File '{file_path}' does not exist.")


if __name__ == "__main__":
    output = "File management works "
    file_manager = FileManagement()
    path = "./temp_data/file_manager.txt"
    file_manager.write_file(output, path)
