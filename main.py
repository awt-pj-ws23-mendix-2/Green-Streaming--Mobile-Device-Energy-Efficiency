from src import power_metrics
from src import parser
from src import cv_player as player
import multiprocessing
import concurrent.futures
import time

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    config_parser = parser.Parser()
    pas = config_parser.get_credentials()
    output = config_parser.get_output_path()
    pd = power_metrics.powermetrics()
    player = player.Player("./testfolder/output.mp4")
    video_path="./testfolder/output.mp4"
    samples = int(player.get_video_total_frames())
    frequency = int(player.get_video_fps())
    print(samples, frequency)
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        # Submit both functions to be executed concurrently
        future2 = executor.submit(pd.gather_data, samples, 1000*(1/frequency), pas, output)
        time.sleep(2)
        future1 = executor.submit(player.play_video, video_path)

        # Wait for both futures to complete
        concurrent.futures.wait([future2, future1])


    print("--------finihed-------")

