from bs4 import BeautifulSoup
import requests

source = requests.get("https://www.billboard.com/charts/hot-100").text

soup = BeautifulSoup(source, "lxml")

top_100_songs = soup.find_all("span", class_= "chart-element__information__song")
top_100_artists = soup.find_all("span", class_= "chart-element__information__artist")

songs = []
artists = []

for x in top_100_songs[0:5]:
    songs.append(x.text)
    
for i in top_100_artists[0:5]:
    artists.append(i.text)
    
zipped = list(zip(songs, artists))

top5 = ""
for index, x in enumerate(zipped):
    top5 += f"{index + 1} {x[0]} by {x[1]} \n"
    
print(top5)


