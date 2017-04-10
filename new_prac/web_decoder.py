import requests
from bs4 import BeautifulSoup

base_url = 'http://www.nytimes.com'
x = requests.get(base_url)
soup = BeautifulSoup(x.text)

for story_heading in soup.find_all(class_="story-heading"):
    if story_heading.a:
        print(story_heading.a.text.replace("\n", " ").strip())
    else:
        print(story_heading.contents[0].strip())
