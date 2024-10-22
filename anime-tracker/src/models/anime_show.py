from .episode import Episode

class AnimeShow:
    def __init__(self, title, genre):
        self.id = None
        self.title = title
        self.genre = genre
        self.episodes = []

    def add_episode(self, episode):
        self.episodes.append(episode)

    def __str__(self):
        return f"{self.title} ({self.genre}) - {len(self.episodes)} episodes"
