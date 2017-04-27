from bs4 import BeautifulSoup

import requests

url = "http://www.espn.com/nfl/draft/rounds"
x = requests.get(url)
soup = BeautifulSoup(x.text, "html.parser")
# print(soup)

for link in soup.find_all(id="draftcast-draftroundresults"):
    print(link.get("draftTable__playerInfo"))
