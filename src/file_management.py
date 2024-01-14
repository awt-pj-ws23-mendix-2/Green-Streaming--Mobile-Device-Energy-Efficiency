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

    @staticmethod
    def find_mp4_files(root_folder):
        mp4_paths = []

        for root, dirs, files in os.walk(root_folder):
            print(f"{root}- {dirs} - {files}")
            for file in files:
                if file.endswith('.mp4'):
                    mp4_paths.append(os.path.join(root, file))

        return mp4_paths

if __name__ == "__main__":
    # output = "File management works "
    file_manager = FileManagement()
    # path = "./temp_data/file_manager.txt"
    # file_manager.write_file(output, path)
    test_folder = "../testfolder"
    mp4_files = file_manager.find_mp4_files(test_folder)

    print("List of .mp4 files:")
    for mp4_file in mp4_files:
        print(mp4_file)