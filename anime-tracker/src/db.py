import json
import os
from src.models.anime_show import AnimeShow
from src.models.episode import Episode

class Database:
    def __init__(self, filename="anime_db.json"):
        self.filename = filename
        self.load()

    def load(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                data = json.load(file)
            self.shows = [AnimeShow(**show) for show in data['shows']]
            for show in self.shows:
                show.episodes = [Episode(**ep) for ep in show.episodes]
        else:
            self.shows = []
        self.save()

    def save(self):
        data = {
            'shows': [{'title': show.title, 'genre': show.genre, 'episodes': [
                {'number': ep.number, 'air_date': ep.air_date.isoformat(), 'watched': ep.watched,
                 'rating': ep.rating, 'review': ep.review} for ep in show.episodes]} for show in self.shows]
        }
        with open(self.filename, 'w') as file:
            json.dump(data, file)

    def add_show(self, title, genre):
        new_show = AnimeShow(title, genre)
        self.shows.append(new_show)
        self.save()

    def get_all_shows(self):
        return self.shows

    def delete_show(self, show_id):
        self.shows = [show for i, show in enumerate(self.shows) if i != show_id]
        self.save()

    def add_episode(self, show_id, episode_number):
        show = self.shows[show_id]
        new_episode = Episode(episode_number)
        show.add_episode(new_episode)
        self.save()

    def mark_episode_watched(self, show_id, episode_id):
        show = self.shows[show_id]
        show.episodes[episode_id].mark_watched()
        self.save()

    def rate_episode(self, show_id, episode_id, rating):
        show = self.shows[show_id]
        show.episodes[episode_id].rate(rating)
        self.save()

    def review_episode(self, show_id, episode_id, review):
        show = self.shows[show_id]
        show.episodes[episode_id].add_review(review)
        self.save()
