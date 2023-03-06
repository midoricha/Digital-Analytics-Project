import pandas as pd
import json
import requests
import pause
import spotifyaudiofeatures

data = pd.read_csv(
    'http://www.digitalanalytics.id.au/static/files/chartdata.csv', sep=';')
data = data.T.to_dict().values()

x = []


for i in data:
    artist = i['artist']
    track = i['track']

    headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer BQDhOzfCl3PRa5cUHYfYDkkeMnC1HePXheTAYikGsP98DxZAM77fOsGTW34OUj7LRbQczEmrz4NImcBgSR1rxCNmci9RB4WnWZimgCWjPOchDYda8W4euB_KrkVMPEzffN3eQICF-iSqjh9mVf-Ki3710NQ0IBI',
    }

    if 'Featuring' in artist:
        artist = artist.split('Featuring')[0]
    if 'featuring' in artist:
        artist = artist.split('featuring')[0]
    if 'Duet' in artist:
        artist = artist.split('Duet')[0]
    if 'x' in artist:
        artist = artist.split('x')[0]
    if 'X' in artist:
        artist = artist.split('X')[0]
    if '&' in artist:
        artist = artist.split('&')[0]
    if 'and' in artist:
        artist = artist.lower().split('and')[0]
    if '/' in artist:
        artist = artist.split('/')[0]
    if 'with' in artist:
        artist = artist.split('with')[0]
    if 'With' in artist:
        artist = artist.split('With')[0]
    if '(' in artist:
        artist = artist.split('(')[0]
    if 'Or' in artist:
        artist = artist.split('Or')[0]

    if '/' in track:
        track = track.split('/')[0]
    if '(' in track:
        track = track.split('(')[0]
    if 'Theme From' in track:
        track = track.remove('Theme From')
    if '$' in track:
        track = track.replace('$', 's')

    query = artist + ' ' + track

    params = (
        ('q', query),
        ('type', 'artist,track'),
    )

    response = requests.get(
        'https://api.spotify.com/v1/search',  headers=headers, params=params)

    print(response)

    json_data = json.loads(response.text)

    try:
        trackid = json_data['tracks']['items'][0]['id']
        print('ok', query)
    except:
        trackid = ''
        print('ERROR', query)

    year = i['year']
    print(str(year) + ' - ' + i['artist'] + ' - ' + i['track'] + trackid)

    pause.seconds(0.05)

    x.append({
        'year': i['year'],
        'artist': i['artist'],
        'track': i['track'],
        'track id': trackid,
    })

x = pd.DataFrame(x)
x.to_csv('spotifyid.csv', sep=';', index=False)
