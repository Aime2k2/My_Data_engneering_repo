import requests
import json
import os
from dotenv import load_dotenv

load_dotenv(dotenv_path='./.env')
API_KEY = os.getenv("API_KEY")
CHANNEL_HANDLE="@MrBeast"
url = ("https://www.googleapis.com/youtube/v3/channels"f"?part=contentDetails&forHandle={CHANNEL_HANDLE}&key={API_KEY}")


def get_playlist_id():
   

    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise HTTPError for bad responses (4xx, 5xx)

        data = response.json()
        # Uncomment to see full JSON responsee ee e 
        # print(json.dumps(data, indent=4))

        channel_items = data['items'][0]
        channel_playlistId = channel_items['contentDetails']['relatedPlaylists']['uploads']

        print("Uploads Playlist ID:", channel_playlistId)
        return channel_playlistId

    except requests.exceptions.RequestException as e:
        print("An error occurred:", e)
        raise e


if __name__ == "__main__":
    get_playlist_id()