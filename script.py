from pyicloud import PyiCloudService
from pyicloud.exceptions import PyiCloudFailedLoginException
from datetime import datetime, timedelta
import os
from dotenv import load_dotenv
import sys

# Load environment variables from .env file
load_dotenv()

# Read username and password from environment variables
username = os.getenv('APPLE_ID')
password = os.getenv('APPLE_PASSWORD')
event_title = os.getenv('EVENT_TITLE')

try:
    # Authenticate
    api = PyiCloudService(username, password)
    if api.requires_2fa:
        print("Two-factor authentication required.")
        code = input("Enter the code you received: ")
        result = api.validate_2fa_code(code)
        print("Code validation result: %s" % result)

        if not result:
            print("Failed to verify security code")
            sys.exit(1)

except PyiCloudFailedLoginException:
    print("Failed to log in to iCloud.")
    exit(1)

# Define the date range for events
from_dt = datetime(2023, 9, 1, 0, 0, 0)
to_dt = from_dt + timedelta(days=30)  # Next 30 days

# Fetch the events
events = api.calendar.events(from_dt, to_dt)

# Count the number of events with a given title
count = 0
for event in events:
    if event['title'] == event_title:
        count += 1

print(f"Number of events with title '{event_title}': {count}")

