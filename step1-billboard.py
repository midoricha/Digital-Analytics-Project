from urllib.request import Request, urlopen
import ssl
from bs4 import BeautifulSoup
import pause
import pandas as pd

x = []

yearnumber = 1970
while yearnumber <= 2020:
    url = 'https://www.billboard.com/charts/year-end/' + \
        str(yearnumber)+'/hot-100-songs'

    headers = {
        'User-Agent': 'Mozilla/5.0 (Macinstosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36(KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    req = Request(url, headers=headers)
    context = ssl._create_unverified_context()

    uClient = urlopen(req, context=context)
    html = uClient.read()
    uClient.close()

    soup = BeautifulSoup(html, 'html.parser')
    divofinterest = soup.find('div', class_='chart-details')

    for i in divofinterest.find_all('div', class_='ye-chart-item__primary-row'):
        artist = i.find(
            'div', class_='ye-chart-item__artist').getText().strip()
        track = i.find('div', class_='ye-chart-item__title').getText().strip()

        print(artist, '-', track)
        print()

        pause.seconds(0.05)

        x.append({
            'year': yearnumber,
            'artist': artist,
            'track': track
        })

    yearnumber += 1

x = pd.DataFrame(x)
x.to_csv('billboard.csv', sep=';', index=False)
