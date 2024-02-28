import cv2
import numpy as np
import ffmpeg
import subprocess
from datetime import datetime

from src.file_management import FileManagement


class Player:

    def __init__(self, video_path):
        self.cap=cv2.VideoCapture(video_path)

    def get_video_end_time(self):
        end_time=0
        end_time = self.get_video_total_frames()/ self.get_video_fps()
        return end_time
    def get_video_fps(self):
        fps=0
        fps = self.cap.get(cv2.CAP_PROP_FPS)

        return fps
    def get_video_total_frames(self):
        total_frames =0
        total_frames = self.cap.get(cv2.CAP_PROP_FRAME_COUNT)
        return total_frames

    def play_video(self, video_path, output_file_path):
        output_file= output_file_path+"_player_logs"
        file_manager = FileManagement()
        output_file_path_count = file_manager.generate_output_file_name(output_file)
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        # play video file in ffmpeg player
        with open(output_file_path_count, 'a') as file:
            file.write(f"\n\n start-Timestamp: {timestamp}\n")
            print(f"\n [video] start-Timestamp: {timestamp}\n")
        sudo_command = f"ffplay -loglevel +repeat -i {video_path} -autoexit 2>>{output_file_path_count}"
        print(sudo_command)
        process = subprocess.Popen(sudo_command, shell=True, universal_newlines=True, stdout=subprocess.PIPE,text=True,stdin=subprocess.PIPE)
        output,error=process.communicate()
        print(f"ffplay {output}")


    def release_detroy(self):
        self.cap.release()
        # self.cv2.destroyAllWindows()
    def get_video_brightness(self, save_file_path):
        brightness_values = []
        timestamp_current = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        while self.cap.isOpened():
            ret, frame = self.cap.read()
            if not ret:
                break
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            val = np.mean(gray)
            brightness_values.append(val)
        output_path = save_file_path+"_brightness"
        file_manager = FileManagement()
        output_file_path_count = file_manager.generate_output_file_name(output_path)

        with open(output_file_path_count, 'a') as file:
            file.write(f"\n start-Timestamp: {timestamp_current} \n")
            file.write(str(brightness_values))
        return brightness_values


# Tests are created to check if the plugin is working as it is intended to be due to issues
# with M1 and M2 mac's
if __name__ == "__test__":
    # Open the video capture
    cap = cv2.VideoCapture('../testfolder/output.mp4')  # Replace 'your_video_file.mp4' with your video file path
    # Check if the video is opened successfully
    if not cap.isOpened():
        print("Error: Could not open video")

    brightness_values = []
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        total_frames = cap.get(cv2.CAP_PROP_FRAME_COUNT)
        brighntenss = cap.get(cv2.CAP_PROP_BRIGHTNESS)
        saturation = cap.get(cv2.CAP_PROP_SATURATION)
        acceleration = cap.get(cv2.CAP_PROP_HW_ACCELERATION)
        color=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Get the current position in milliseconds
        timestamp_msec = cap.get(cv2.CAP_PROP_POS_MSEC)
        fps = cap.get(cv2.CAP_PROP_FPS)
        video_end_time=total_frames/fps # duration in seconds
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        val=np.mean(gray)
        brightness_values.append(val)


        # Convert milliseconds to a readable time format
        current_time = int(timestamp_msec / 1000)  # Convert to seconds
        minutes = current_time // 60
        seconds = current_time % 60
        hours = minutes // 60
        minutes = minutes % 60

        # Print the current time
        print(f"Current Time: {hours:02d}:{minutes:02d}:{seconds:02d} ++ {fps} ++ {total_frames} __{brighntenss}__{saturation}")

        # Show the frame (optional)
        cv2.imshow('Frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    print(f"{brightness_values} length{len(brightness_values)}")
    # Release the video capture and close windows
    cap.release()
    cv2.destroyAllWindows()

    print("starting with ffplay ")
    player= Player('../testfolder/output.mp4')
    player.play_video('../testfolder/output.mp4')

# check if the streaming is supported in the sense of online streaming
# rather than downloading video locally and playing it.
if __name__=="__main__":
    print("Starting the online streaming video class ....")

    video_path = 'https://refcontent.s3.eu-central-1.amazonaws.com/ref_content/luminance/GS_luma_filter_0_to_100_in_60sec_steps.mp4'
    player = Player(video_path)
    brightness_values = player.get_video_brightness("./temp_data/output")
    print(f"lenght: {len(brightness_values)} \n{brightness_values}")
