import re
import os


class FileManagement:
    def __init__(self):
        pass

    def get_filename(self, path):
        match = re.search(r'([^/\\]+)\.mp4$', path)
        return match.group(1)

    @staticmethod
    def generate_output_file_name(base_name):
        count = 1
        file_name = f"{base_name}_{count}.txt"
        while os.path.exists(file_name):
            file_name = f"{base_name}_{count}.txt"
            count += 1
        return file_name
    def write_file(self, output, file_path):
        if os.path.exists(file_path):
            with open(file_path, 'a') as file:
                file.write(output)
            print(f"Data successfully written to {file_path}")
        else:
            print(f"Error: File '{file_path}' does not exist.")

    # {number_of_files} defines number of video which needs to be played . "000" means all videos needs to be
    #     player locally
    @staticmethod
    def find_mp4_files(root_folder, number_of_files=1):
        mp4_paths = []

        for root, dirs, files in os.walk(root_folder):
            print(f"{root}- {dirs} - {files}")
            for file in files:
                if file.endswith('.mp4'):
                    mp4_paths.append(os.path.join(root, file))

            if(number_of_files == 000):
                 mp4_paths = mp4_paths
            else:
                mp4_paths= mp4_paths[:number_of_files]
        return mp4_paths
    @staticmethod
    def online_video_links(path_to_file_stored_video_links, number_of_links=1):
        with open(path_to_file_stored_video_links, 'r') as file:
            links = [line.strip() for line in file.readlines()]
        return links[:number_of_links]



        pass
if __name__ == "__test__":
    output = "File management works "
    file_manager = FileManagement()
    path = "./temp_data/file_manager.txt"
    file_manager.write_file(output, path)
    test_folder = "../testfolder"
    mp4_files = file_manager.find_mp4_files(test_folder, 000)

    print("List of .mp4 files:")
    for mp4_file in mp4_files:
        print(mp4_file)

    # New links reading function test

    online_links=file_manager.online_video_links("../video_links.txt")
    print(online_links)


    #  file name check
    filename=file_manager.get_filename(online_links[0])
    print("filename",filename)