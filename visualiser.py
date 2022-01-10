#https://spotipy.readthedocs.io/en/2.19.0/ quickstart
#https://developer.spotify.com/documentation/web-api/ docs
import spotipy
import json
import pandas as pd
from spotipy.oauth2 import SpotifyOAuth

scope = "playlist-read-collaborative"
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))
#global variables
#(env) [marcin@marcin-ms7c91 env]$ export SPOTIPY_CLIENT_SECRET=''
#(env) [marcin@marcin-ms7c91 env]$ export SPOTIPY_CLIENT_ID=''
#(env) [marcin@marcin-ms7c91 env]$ export SPOTIPY_REDIRECT_URI='http://localhost:8080'

#source /Pulpit/projekt/bin/activate


playlist_id="1DZNglILKZAcJD81SmELHQ"
results = sp.playlist_items(playlist_id, fields=None, limit=100, offset=0, market=None, additional_types=('track', 'episode'))
items = results['items']



with open('data.json', 'w') as f:
    json.dump(items, f)


for track in results['items']:
     dict = track['track']
     x=dict['id']
     s = json.dumps(dict)
    
     print(type(x))
     print()




df = pd.read_json('data.json')
#print(df.to_string())
top=df.head()
print(top)
df.to_csv('nasze_dane.csv')
#for idx, item in enumerate(results['items']):
     #print(results)
    #  track = item['track']
    #  print(idx, track['artists'][0]['name'], " – ", track['name'])
