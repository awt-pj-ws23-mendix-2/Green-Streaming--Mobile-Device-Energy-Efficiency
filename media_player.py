import ffmpeg
import ffmpeg as ff
import subprocess

def play_video(video_path):
    # command = ['ffplay -loglevel ', video_path]
    # subprocess.call(command)
    sudo_command = f"ffplay -loglevel +repeat -i {video_path}"
    print(sudo_command)
    # output = subprocess.check_output(sudo_command, shell=True, universal_newlines=True ,input='2252')
    output = subprocess.run(sudo_command, shell=True, universal_newlines=True, stdout=subprocess.PIPE,
                            text=True)
    print(output)

if __name__ == '__main__':
    stream = ff.input("./output.mp4")
    probe = ffmpeg.probe("./output.mp4")
    print(probe)
    print(probe['streams'])
    video_info = next(s for s in probe['streams'] if s['codec_type'] == 'video')
    print(video_info)
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
