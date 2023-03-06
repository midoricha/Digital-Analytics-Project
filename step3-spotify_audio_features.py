import pandas as pd
import json
import requests
import pause

data = pd.read_csv('spotifyid.csv', sep=';')
data = data.T.to_dict().values()

y = []

for i in data:
    query = i['track id']

    headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer BQCKofAdcjd6Pcbz_OMJKq-oBPqhCt_GONv7MBBU95-Q65M8wI42atkUXFBFCW2KLb3-6bcdYYpW9D-H1iKCs3noMpqKGAdOdDfMmb7ZgGb9LpGiOaq6xtQDl_oiw7NMzv9ugB49Bv6DbYKBRzGXYJexCW3_5Og',
    }

    url = 'https://api.spotify.com/v1/audio-features/' + str(query)

    response = requests.get(url, headers=headers)

    print(response)

    json_data = json.loads(response.text)

    year = i['year']
    print(str(year) + ' - ' + i['artist'] + ' - ' + i['track'])

    try:
        danceability = json_data['danceability']
    except:
        danceability = ''

    print(danceability)

    try:
        energy = json_data['energy']
    except:
        energy = ''

    print(energy)

    try:
        loudness = json_data['loudness']
    except:
        loudness = ''

    print(loudness)

    try:
        acousticness = json_data['acousticness']
    except:
        acousticness = ''

    print(acousticness)

    pause.seconds(0.1)

    y.append({
        'year': i['year'],
        'artist': i['artist'],
        'track': i['track'],
        'track id': i['track id'],
        'danceability': danceability,
        'energy': energy,
        'loudness': loudness,
        'acousticness': acousticness,
    })

y = pd.DataFrame(y)
y.to_csv('spotify-audio-features.csv', sep=';', index=False)
