# Step 1: Log Into Youtube
# Step 2: Grab Liked Videos
# Step 3: Create A New Playlist
# Step 4: Search For The Song
# Step 5: Add Song Into The New Spotify Playlist


# Required APIs:
# 1. Youtube API
# 2. Spotify API
# 3. Youtube-dl Library: https://github.com/ytdl-org/youtube-dl

import json

class CreatePlaylists:
    
    def __init__(self):
        self.user_id = spotify_user_id
        self.spotify_token = spotify_token

    # Step 1: Log Into Youtube
    def get_youtube_client(self):
        pass

    # Step 2: Grab Liked Videos
    def get_liked_videos(self):
        pass

    # Step 3: Create A New Playlist
    def create_playlist(self):
        
        request_body = json.dumps({
            "name": "YouTube Liked Videos",
            "description":"All Liked YouTube Videos",
            "public": False
        })

        query = "https://api.spotify.com/v1/users/{}/playlists".format(self.user_id)
        response = requests.post(
            query,
            data = request_body,
            headers = {
                "Content-Type": "application/json",
                "Authorization": "Bearer {}".format(spotify_token)
            }
        )
        response_json = response.json()

        #playlist ID
        return response.json["id"]

    # Step 4: Search For The Song
    def get_spotify_uri(self, song_name, artist):
               query = "https://api.spotify.com/v1/search?query=track%3A{}+artist%3A{}&type=track&offset=0&limit=20".format(
            song_name,
            artist
        )
        response = requests.get(
            query,
            headers={
                "Content-Type": "application/json",
                "Authorization": "Bearer {}".format(spotify_token)
            }
        )
        response_json = response.json()
        songs = response_json["tracks"]["items"]

        # only use the first song
        uri = songs[0]["uri"]

        return uri

    # Step 5: Add This Song Into The New Spotify Playlist
    def add_song_to_playlist(self):
        pass

