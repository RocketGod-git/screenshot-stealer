import requests
import string
import random
import time
import os
import sys
import json
from keep_alive import keep_alive

# Load configuration from config.json
with open("config.json", "r") as file:
    config = json.load(file)
    discord_webhook_url = config["discord_webhook_url"]

# Start the Flask server to keep the script alive
keep_alive()

# Continuously generate and send random URLs to Discord webhook
while True:
    try:
        # Generate a random string of 5 lowercase characters
        random_suffix = "".join(random.choices(string.ascii_lowercase, k=5))

        # Prepend the suffix with "s"
        random_string = "s" + random_suffix

        # Print the current random string being tested
        print(f"Testing {random_string}...")

        # Get the URL of the subdirectory
        url = "https://prnt.sc/" + random_string

        # Send the URL to the Discord webhook using requests.post()
        payload = {"content": f"Sent to URL: {url}"}
        response = requests.post(discord_webhook_url, data=payload)

        # Check if the response was successful
        if response.ok:
            print(f"Sent to URL: {url}")
        else:
            print(f"Failed to send URL: {url}")

        # Sleep for 1 second before generating the next URL
        time.sleep(1)

    except Exception as e:
        # Print any exceptions that occur
        print(f"Exception occurred: {e}")

        # Wait for 30 seconds before restarting the loop
        time.sleep(30)

        # Restart the script
        python = sys.executable
        os.execl(python, python, *sys.argv)
