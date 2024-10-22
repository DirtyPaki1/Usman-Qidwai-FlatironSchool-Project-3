from src.db import Database

db = Database()

def display_shows():
    shows = db.get_all_shows()
    print("\nAvailable Anime Shows:")
    for i, show in enumerate(shows, start=1):
        print(f"{i}. {show}")

def display_episodes(show):
    print("\nEpisodes:")
    for i, episode in enumerate(show.episodes, start=1):
        watched_status = "Watched" if episode.watched else "Not Watched"
        print(f"{i}. {episode.number} ({watched_status})")

def get_user_input(prompt, type=str):
    while True:
        try:
            return type(input(prompt))
        except ValueError:
            print("Invalid input. Please try again.")

def get_positive_int(prompt):
    while True:
        num = get_user_input(prompt, int)
        if num > 0:
            return num
        print("Please enter a positive integer.")
