import ffmpeg


class VideoPlayer:

    codec ='h264'
    def __init__(self,video_path, codec):
        self.video_path = video_path
        self.codec = codec
    def play_video(self):
        ffmpeg.run()

    @classmethod
    def changeCodec(cls, codec):
        cls.codec = codec
