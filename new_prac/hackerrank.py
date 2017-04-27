import requests
from bs4 import BeautifulSoup

base_url = "https://cdn.hackerrank.com/hackerrank/static/contests/capture-the-flag/secret/key.json"
x = requests.get(base_url)
soup = BeautifulSoup(x.text)
print(soup)

# for story_heading in soup.find_all(class_="news-body"):
#     if story_heading.a:
#         print(story_heading.a.text.replace("\n", " ").strip())
#     else:
#         print(story_heading.contents[0].strip())
