from bs4 import BeautifulSoup

import requests

round_num = input("What round would you like to see:\n>")
url = "http://www.espn.com/nfl/draft/rounds/_/round/{}".format(round_num)
x = requests.get(url)
soup = BeautifulSoup(x.text, "html.parser")
# print(soup)
num = 1

print("Round {} of 2017 NFL Draft\n".format(round_num))

## This is the first way, just the name and college!
# for draftTable__headline in soup.find_all(class_="draftTable__playerInfo"):
#     print(num, draftTable__headline.text.replace("\n", " ").strip())
#     num+=1

## This is for the name, college and position
for draftTable__headline in soup.find_all(class_="draftTable__headline"):
    print(draftTable__headline.text.replace("\n", " ").strip())
