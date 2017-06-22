from bs4 import BeautifulSoup
import time
import requests

# Another scrape but for the NBA Draft 2017
rd_num = input("Which Round of the NBA Draft do you want to see? 1 or 2?\n>")
url = "http://www.espn.com/nba/draft/rounds/_/round/{}".format(rd_num)
page = requests.get(url)
soup = BeautifulSoup(page.text, "html.parser")

print("Round {} of the 2017 NBA Draft".format(rd_num))

for draftTable__headline in soup.find_all(class_="draftTable__headline"):
    team = str(draftTable__headline.img).upper()
    team = team[79:82] #or 69:72
    print(team, draftTable__headline.text.replace("\n", " ").strip())
    time.sleep(1)
