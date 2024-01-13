import re

class FileManagement:
    def __init__(self):
        pass

    def get_filename(self,path):
        match = re.search(r'([^/\\]+)\.mp4$', path)
        return match.group(1)


if __name__=="__main__":
    video_path = "./testfolder/output.mp4"

    # Use regular expression to extract the word before ".mp4"
    match = re.search(r'([^/\\]+)\.mp4$', video_path)

    if match:
        word_before_mp4 = match.group(1)
        print("Word before .mp4:", word_before_mp4)
    else:
        print(".mp4 extension not found in the given path.")

    print(word_before_mp4+".txt")