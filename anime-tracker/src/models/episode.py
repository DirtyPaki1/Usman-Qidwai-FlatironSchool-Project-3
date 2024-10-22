from datetime import date

class Episode:
    def __init__(self, number, air_date=None):
        self.id = None
        self.number = number
        self.air_date = air_date or date.today()
        self.watched = False
        self.rating = None
        self.review = ""

    def mark_watched(self):
        self.watched = True

    def rate(self, rating):
        self.rating = rating

    def add_review(self, review):
        self.review = review

    def __str__(self):
        watched_status = "Watched" if self.watched else "Not Watched"
        return f"Episode {self.number} ({watched_status}) - Air Date: {self.air_date}"
