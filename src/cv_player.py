import cv2
import numpy as np
import ffmpeg
import subprocess

class Player:

    def __init__(self, video_path):
        pass

    def get_video_end_time(self):
        end_time=0
        return end_time
    def get_video_fps(self):
        fps=0
        return fps
    def get_video_total_frames(self):
        total_frames =0
        return total_frames

    def play_video(self, video_path):
        # code for playing the frames one at a time

        # cap.release()
        # cv2.destroyAllWindows()
        pass

        sudo_command = f"ffplay -loglevel +repeat -i {video_path} "
        print(sudo_command)
        output = subprocess.run(sudo_command, shell=True, universal_newlines=True, stdout=subprocess.PIPE,
                                text=True)
        print(output)



if __name__ == "__main__":
    # Open the video capture
    # cap = cv2.VideoCapture('../testfolder/Randhom HD/random_HD_25fps_25Mbps_H264.mp4')  # Replace 'your_video_file.mp4' with your video file path
    cap = cv2.VideoCapture('../testfolder/output.mp4')  # Replace 'your_video_file.mp4' with your video file path
    # Check if the video is opened successfully
    if not cap.isOpened():
        print("Error: Could not open video")

    brightness_values = []
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        # cv2.imshow('Video Player', frame)
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
        # print(f"color {color}__ {acceleration}")


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