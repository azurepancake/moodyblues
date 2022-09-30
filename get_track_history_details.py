import requests
import pandas as pd

CLIENT_ID = '4d2f8e0410a34333944079dffed19d6b'
CLIENT_SECRET = 'dfa1149a98a1450ea7fce5211bc33908'
AUTH_URL = 'https://accounts.spotify.com/api/token'
BASE_URL = 'https://api.spotify.com/v1/'

# POST to get token
auth_response = requests.post(AUTH_URL, {
    'grant_type': 'client_credentials',
    'scope': 'user-read-recently-played',
    'client_id': CLIENT_ID,
    'client_secret': CLIENT_SECRET
})

# Convert the response to JSON
auth_response_data = auth_response.json()

# Save the access token
access_token = auth_response_data['access_token']

# Load headers with access token
headers = {'Authorization': 'Bearer {token}'.format(token=access_token)} # This is not passing scope properly
headers = {'Authorization': 'Bearer BQDMa-jVEMOoM2q-WRNIaEfh8f001mW9JQoFDu0d4zbDDMvNy8q3u-ZUOHHuwHV9qegNPcay_cxKQeVOJfz76I38oxDPkliPJhSQ14ukdtEy7Mu52EyC-eRiwCb7rSZ1HnJr2xI2s-d_mIO66tE8KkFIS19z5Mu1Liss_TmNaIMXWnpAHw8'}

# Get recently played tracks
r = requests.get(BASE_URL + 'me/player/recently-played', headers=headers)
r = r.json()

artists = []
albums = []
songs = []

track_data = r['items']
for track in track_data:
    songs.append(track['track']['name'])
    albums.append(track['track']['album']['name'])
    artists.append(track['track']['album']['artists'][0]['name'])


track_data_dict = {
    "songs" : songs,
    "albums" : albums,
    "artists" : artists
}

track_df = pd.DataFrame(track_data_dict)

print(track_df)
