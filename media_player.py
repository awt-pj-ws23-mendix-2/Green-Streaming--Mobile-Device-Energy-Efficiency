import ffmpeg
import ffmpeg as ff
import subprocess

def play_video(video_path):
    command = ['ffplay', video_path]
    subprocess.call(command)
class Car:

    def __init__(self, speed=0):
        self.speed = speed
        self.odometer = 0
        self.time = 0

    def accelerate(self):
        self.speed += 5

    def brake(self):
        self.speed -= 5

    def step(self):
        self.odometer += self.speed
        self.time += 1

    def average_speed(self):
        return self.odometer / self.time


if __name__ == '__main__':
    stream = ff.input("./output.mp4")
    probe = ffmpeg.probe("./output.mp4")
    print(probe)
    print(probe['streams'])
    video_info = next(s for s in probe['streams'] if s['codec_type'] == 'video')

    # Get the average and peak brightness
    avg_brightness = video_info.get('avg_frame_level', {}).get('brightness')
    peak_brightness = video_info.get('max_frame_level', {}).get('brightness')
    path= "./output.mp4"
    print(avg_brightness)
    print("playing video")
    play_video("./output.mp4")
    print("done calling video")
    # sudo_command_2 = f"open -a VLC {path}"
    # output = subprocess.check_output(sudo_command_2, shell=True, universal_newlines=True)
    # print(output)
    # output_stream = ffmpeg.output(stream, 'dummy', f='rawvideo')
    # ff.run(output_stream)
    # ff.run(stream)
