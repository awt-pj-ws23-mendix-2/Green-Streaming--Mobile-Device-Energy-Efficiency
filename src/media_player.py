import ffmpeg
import ffmpeg as ff
import subprocess

def play_video(video_path):
    # command = ['ffplay -loglevel ', video_path]
    sudo_command = f"ffplay -loglevel +repeat -i {video_path} "
    print(sudo_command)
    output = subprocess.run(sudo_command, shell=True, universal_newlines=True, stdout=subprocess.PIPE,
                            text=True)
    print(output)

if __name__ == '__main__':
    stream = ff.input("../testfolder/output.mp4")

    play_video("../testfolder/output.mp4")















