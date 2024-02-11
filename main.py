from src import power_metrics
from src import parser
from src import cv_player as player
import concurrent.futures
import time
from src import file_management
from datetime import datetime
from src import extractor

def initialize():
    # get configurations
    config_parser = parser.Parser()
    pas = config_parser.get_credentials()

    # all the requirement for main will be initialized here
    file_manager = file_management.FileManagement()
    video_path = file_manager.find_mp4_files("./testfolder", 1)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    local_execution = True
    #  get configurations
    config_parser = parser.Parser()
    pas = config_parser.get_credentials()

    # all the requirement for main will be initialized here
    file_manager = file_management.FileManagement()
    if local_execution:
        video_paths = file_manager.find_mp4_files("./testfolder", 1)
    else:
        print(f" online links are activated for input ")
        video_paths = file_manager.online_video_links("./video_links.txt", 1)
    print(f"total mp4 files to play :{len(video_paths)}")
    for video_path in video_paths:
        print(f"Playing video {video_path}")
        file_name = file_manager.get_filename(video_path)

        #  intialize player
        player = player.Player(video_path)

        #  video realted informtion to gatgher metrices
        output = config_parser.get_output_path() + file_name
        samples = int(player.get_video_total_frames())
        frequency = int(player.get_video_fps())
        interval = int(1000 * (1 / frequency))
        print(f"samples:{samples}, frequency: {frequency}")
        pd = power_metrics.Powermetrics()
        # player.get_video_brightness(output)
        with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            print(f"concurrent tasks starting : {timestamp}")
            future_1 = executor.submit(player.get_video_brightness,output)
            # Submit  functions to be executed concurrently
            future2 = executor.submit(pd.gather_data, samples, interval, pas, output)
            time.sleep(2)
            future1 = executor.submit(player.play_video, video_path, output)
            # Wait for futures to complete
            concurrent.futures.wait([future2, future1, future_1])

        timestamp= datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"concurrent tasks ending : {timestamp}")

        print("--------finished-------")
        player.release_detroy()

        extractor = extractor.Extractor()
        temp_data_folder = 'src/temp_data'
        csv_output_folder = 'src/csv_output'
        extractor.process_video_files(temp_data_folder, csv_output_folder)
