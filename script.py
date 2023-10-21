from dotenv import load_dotenv
import os
import subprocess

# Load environment variables from .env file
load_dotenv()

# Read EVENT_TITLE from .env
search_title = os.getenv("EVENT_TITLE")

def get_today_events():
    script_path = "./get_events.applescript"
    output = subprocess.check_output(["osascript", script_path])
    event_titles = output.decode("utf-8").strip().split(", ")
    return event_titles

def count_events_by_title(event_titles, search_title):
    return event_titles.count(search_title)

if __name__ == "__main__":
    event_titles = get_today_events()
    count = count_events_by_title(event_titles, search_title)
    print(f"There are {count} events with the title '{search_title}' today.")
