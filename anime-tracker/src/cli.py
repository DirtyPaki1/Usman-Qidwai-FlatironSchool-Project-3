import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.db import Database
from src.helpers import display_shows, display_episodes, get_user_input, get_positive_int

db = Database()

def main_menu():
    print("\nAnime Tracker Menu")
    print("1. View All Shows")
    print("2. Add New Show")
    print("3. Exit")
    choice = get_user_input("> ", int)
    
    if choice == 1:
        view_shows()
    elif choice == 2:
        add_new_show()
    elif choice == 3:
        print("Goodbye!")
        sys.exit(0)
    else:
        print("Invalid choice. Please try again.")
        main_menu()

def view_shows():
    shows = db.get_all_shows()
    if not shows:
        print("No anime shows available.")
        main_menu()
    
    display_shows()
    show_choice = get_positive_int("Enter the number of the show to view details: ")
    if show_choice <= len(shows):
        selected_show = shows[show_choice - 1]
        print(f"\n{selected_show}")
        display_episodes(selected_show)
        
        while True:
            print("\nOptions:")
            print("1. Add Episode")
            print("2. Mark Episode as Watched")
            print("3. Rate Episode")
            print("4. Review Episode")
            print("5. Delete Show")
            print("6. Back to Main Menu")
            
            action = get_user_input("Choose an option: ", int)
            if action == 1:
                episode_number = get_positive_int("Enter episode number: ")
                db.add_episode(shows.index(selected_show), episode_number)
                print("Episode added successfully.")
            elif action == 2:
                episode_choice = get_positive_int("Enter the number of the episode to mark as watched: ")
                if episode_choice <= len(selected_show.episodes):
                    db.mark_episode_watched(shows.index(selected_show), episode_choice - 1)
                    print("Episode marked as watched.")
                else:
                    print("Invalid episode number.")
            elif action == 3:
                episode_choice = get_positive_int("Enter the number of the episode to rate: ")
                if episode_choice <= len(selected_show.episodes):
                    rating = get_user_input("Enter rating (1-10): ", float)
                    db.rate_episode(shows.index(selected_show), episode_choice - 1, rating)
                    print("Episode rated successfully.")
                else:
                    print("Invalid episode number.")
            elif action == 4:
                episode_choice = get_positive_int("Enter the number of the episode to review: ")
                if episode_choice <= len(selected_show.episodes):
                    review = input("Enter your review: ")
                    db.review_episode(shows.index(selected_show), episode_choice - 1, review)
                    print("Review added successfully.")
                else:
                    print("Invalid episode number.")
            elif action == 5:
                confirm = input("Are you sure you want to delete this show? (y/n): ").lower()
                if confirm == 'y':
                    db.delete_show(shows.index(selected_show))
                    print("Show deleted successfully.")
                    break
                else:
                    print("Deletion cancelled.")
            elif action == 6:
                break
            else:
                print("Invalid option. Please choose again.")
    else:
        print("Invalid show number.")
    main_menu()

def add_new_show():
    title = input("Enter anime show title: ")
    genre = input("Enter anime genre: ")
    db.add_show(title, genre)
    print(f"Anime show '{title}' added successfully.")
    main_menu()

if __name__ == "__main__":
    main_menu()
