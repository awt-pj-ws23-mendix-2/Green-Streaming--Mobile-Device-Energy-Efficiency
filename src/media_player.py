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
    stream = ff.input("../output.mp4")

    play_video("../output.mp4")















