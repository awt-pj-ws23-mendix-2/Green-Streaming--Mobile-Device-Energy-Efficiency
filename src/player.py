import subprocess
import os
import cv2
import numpy as np


def play_video(video_path):
    subprocess.run(['ffplay', '-autoexit', video_path])
print(os.getcwd())
video_folder = '../testfolder'
video_files = [f for f in os.listdir(video_folder) if f.endswith('.mp4')]

for video_file in video_files:
    play_video(os.path.join(video_folder, video_file))
    input("Press Enter to play the next video...")


def calculate_brightness(video_path, start_time, end_time):
    cap = cv2.VideoCapture(video_path)
    fps = cap.get(cv2.CAP_PROP_FPS)
    start_frame = int(start_time * fps)
    end_frame = int(end_time * fps)
    brightness_values = []

    cap.set(cv2.CAP_PROP_POS_FRAMES, start_frame)

    while cap.get(cv2.CAP_PROP_POS_FRAMES) < end_frame:
        ret, frame = cap.read()
        if not ret:
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        brightness_values.append(np.mean(gray))

    cap.release()

    if brightness_values:
        return np.mean(brightness_values)
    else:
        return "No brightness information found"

# Usage of the brightness measure method
# video_path = 'abc.mp4'
# start_time = 10
# end_time = 20
# average_brightness = calculate_brightness(video_path, start_time, end_time)
# print("Average Brightness from", start_time, "to", end_time, "seconds:", average_brightness)



def get_video_fps(video_path):
    cap = cv2.VideoCapture(video_path)
    fps = cap.get(cv2.CAP_PROP_FPS)
    cap.release()
    return fps

# Usage of the fps measure method
# video_path = 'abc.mp4'
# fps = get_video_fps(video_path)
# print("FPS:", fps)


def get_video_resolution(video_path):
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        return "Cannot open video"

    width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
    height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
    cap.release()
    print(f"width {width},{height}")
    return int(width), int(height)

video_path = 'testfolder/output.mp4'
resolution = get_video_resolution(video_path)
print(f"Resolution: {resolution[0]}x{resolution[1]}")
