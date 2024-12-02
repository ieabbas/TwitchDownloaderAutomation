import os
import subprocess
import requests
from datetime import datetime, timedelta
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Twitch API credentials
CLIENT_ID = os.getenv("TWITCH_CLIENT_ID")
OAUTH_TOKEN = os.getenv("TWITCH_OAUTH_TOKEN")
BASE_URL = "https://api.twitch.tv/helix"

# Time range for highlights (last 48 hours)
NOW = datetime.utcnow()
TWO_DAYS_AGO = NOW - timedelta(hours=48)
START_TIME = TWO_DAYS_AGO.strftime("%Y-%m-%dT%H:%M:%SZ")

# Function to fetch highlights
def fetch_highlights(user_id):
    url = f"{BASE_URL}/videos"
    headers = {
        "Client-ID": CLIENT_ID,
        "Authorization": f"Bearer {OAUTH_TOKEN}"
    }
    params = {
        "user_id": user_id,
        "type": "highlight",
        "started_at": START_TIME,
        "first": 100  # Maximum results per page
    }
    
    response = requests.get(url, headers=headers, params=params)
    if response.status_code != 200:
        raise Exception(f"Error fetching highlights: {response.status_code} - {response.json()}")
    
    return response.json().get("data", [])

# Function to download a highlight
def download_highlight(video_id, output_dir):
    output_path = os.path.join(output_dir, f"{video_id}.mp4")
    subprocess.run([
        "TwitchDownloaderCLI", "video",
        "-id", video_id,
        "-o", output_path
    ])
    print(f"Downloaded highlight {video_id} to {output_path}")

# Main script
def main():
    # Get your Twitch user ID
    user_url = f"{BASE_URL}/users"
    headers = {
        "Client-ID": CLIENT_ID,
        "Authorization": f"Bearer {OAUTH_TOKEN}"
    }
    user_response = requests.get(user_url, headers=headers)
    if user_response.status_code != 200:
        raise Exception(f"Error fetching user ID: {user_response.status_code} - {user_response.json()}")
    
    user_id = user_response.json()["data"][0]["id"]
    print(f"Fetched user ID: {user_id}")

    # Fetch highlights from the last 48 hours
    highlights = fetch_highlights(user_id)
    print(f"Found {len(highlights)} highlights from the last 48 hours.")

    # Download each highlight
    output_dir = "twitch_highlights"
    os.makedirs(output_dir, exist_ok=True)
    for highlight in highlights:
        download_highlight(highlight["id"], output_dir)

    print("All highlights downloaded successfully!")

if __name__ == "__main__":
    main()
