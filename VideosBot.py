class VideosBot:
    def __init__(self):
        self.videos = []
        self.videosIndex = None
        self.videosCount = None
        self.init_videos()

    def init_videos(self):
        videos_file = open("videos", "r")
        self.videos = videos_file.read().splitlines()
        self.videosCount = len(self.videos)

    def get_next_video(self):
        self.iterate_index()
        return self.videos[self.videosIndex]

    def iterate_index(self):
        if self.videosIndex is None:
            self.videosIndex = 0
        else:
            self.videosIndex = (self.videosIndex + 1) % self.videosCount
