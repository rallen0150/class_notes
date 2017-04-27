from bs4 import BeautifulSoup

import requests

round_num = input("What round would you like to see:\n>")
url = "http://www.espn.com/nfl/draft/rounds/_/round/{}".format(round_num)
x = requests.get(url)
soup = BeautifulSoup(x.text, "html.parser")
# print(soup)
num = 1

print("\nRound {} of 2017 NFL Draft\n".format(round_num))

for link in soup.find_all(id="draftcast-draftroundresults"):
    print(num, link.get("draftTable__playerInfo"))
    num+=1
