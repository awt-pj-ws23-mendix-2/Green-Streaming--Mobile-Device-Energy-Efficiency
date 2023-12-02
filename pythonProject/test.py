import ffmpeg as ff


class VideoPlayer:
    codec = 'h264'  # Default

    def __init__(self, video_path, codec):
        self.video_path = video_path
        self.codec = codec

    def play_video(self):
        start_time = '00:00:10'  # Start time for trimming (HH:MM:SS)
        end_time = '00:00:20'
        stream = ff.input(self.video_path)
        stream = ff.hflip(stream)
        stream = ff.output(stream, './asset/output.mp4')
        ff.run(stream)

    @classmethod
    def change_codec(cls, codec):
        cls.codec = codec


v = VideoPlayer("./asset/sample_h264.mp4", "h264")

v.play_video()
