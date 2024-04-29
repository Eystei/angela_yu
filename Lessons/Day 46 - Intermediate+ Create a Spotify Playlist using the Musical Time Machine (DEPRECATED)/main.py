from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth, SpotifyClientCredentials

answer_year = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD\n>...")

response = requests.get(f"https://www.billboard.com/charts/hot-100/{answer_year}/")
site_html = response.text

soup = BeautifulSoup(site_html, "html.parser")
song_names_selector = soup.select("li > h3#title-of-a-story")
song_names = [item.getText().strip() for item in song_names_selector]


CLIENT_ID = "fb*****87dc47ad867da5d47aea069f"
CLIENT_SECRET = "23******7794e48b4ac0e95db6d7a2c7c"
REDIRECT_URI = "http://localhost:8888/callback"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
                                               client_id="CLIENT_ID",
                                               client_secret="CLIENT_SECRET",
                                               redirect_uri="REDIRECT_URI",
                                               scope="playlist-modify-private",
                                               show_dialog=True,
                                               cache_path="token.txt",
                                               username="YB"))

user_id = sp.current_user()["id"]