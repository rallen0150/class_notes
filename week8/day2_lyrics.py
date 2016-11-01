import requests
import time
from bs4 import BeautifulSoup

headers = {
    "user-agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36'
}

#################### Search for a band
search_url = 'http://search.azlyrics.com/search.php?q='
artist = 'michael+jackson'
body = requests.get(search_url + artist)
souper = BeautifulSoup(body.text, "html.parser")
# print(body.text)
all_a_tags = souper.findAll('a')
next_page = all_a_tags[28].get('href')

# time.sleep(2)

#################### Find all songs
body = requests.get(next_page, headers=headers)
souper = BeautifulSoup(body.text, 'html.parser')
all_a_tags = souper.findAll('a')[35:284]
song_link_list = []

for counter, tag in enumerate(all_a_tags):
    if not tag.get('rel') and tag.get('href'):
        song_link_list.append(tag.get('href'))

for song_link in song_link_list:
    new_song_link = song_link.replace("..", 'http://www.azlyrics.com')
    song_page = requests.get(new_song_link, headers=headers)
    souper = BeautifulSoup(song_page.text, 'html.parser')
    song_divs = souper.findAll('div')[22]
    print(song_divs.text)
    # for counter, div in enumerate(all_divs):
    #     print(counter, div)
    input()
