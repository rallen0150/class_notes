from bs4 import BeautifulSoup
import time
import requests

round_num = input("What round would you like to see:\n>")
url = "http://www.espn.com/nfl/draft/rounds/_/round/{}".format(round_num)
x = requests.get(url)
soup = BeautifulSoup(x.text, "html.parser")
# print(soup)
num = 1

print("Round {} of 2017 NFL Draft".format(round_num))

## This is the first way, just the name and college!
# for draftTable__headline in soup.find_all(class_="draftTable__playerInfo"):
#     print(num, draftTable__headline.text.replace("\n", " ").strip())
#     num+=1

## This is for the name, college and position
for draftTable__headline in soup.find_all(class_="draftTable__headline"):
    ## Way to get the team's initials
    a = str(draftTable__headline.img).upper()
    a = a[79:82]
    print(a, draftTable__headline.text.replace("\n", " ").strip())

    # if a.startswith("http://a1.espncdn.com/combiner/i?img=/i/teamlogos/nfl/500/scoreboard/"):
    #     print(a[69:72])
    # time.sleep(1) #If I want a slow delay, for after the draft
