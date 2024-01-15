from src import power_metrics
from src import parser
from src import cv_player as player
import concurrent.futures
import time
from src import file_management
def initialize():
    # all the requirement for main will be initialized here
    pass

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    config_parser = parser.Parser()
    pas = config_parser.get_credentials()
    pd = power_metrics.powermetrics()
    video_path="./testfolder/output.mp4"
    # demo tryout a new naming method
    file_manager= file_management.FileManagement()
    file_name=file_manager.get_filename(video_path)
    output = config_parser.get_output_path()+file_name
    player = player.Player(video_path)
    samples = int(player.get_video_total_frames())
    frequency = int(player.get_video_fps())
    interval = int(1000*(1/frequency))
    print(samples, frequency)
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        # Submit both functions to be executed concurrently
        future2 = executor.submit(pd.gather_data, samples, interval, pas, output)
        time.sleep(2)
        future1 = executor.submit(player.play_video, video_path, output)
        # Wait for both futures to complete
        concurrent.futures.wait([future2, future1])

    print("--------finished-------")
    player.release_detroy()

