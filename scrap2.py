import requests
from bs4 import BeautifulSoup

r = requests.get("https://www.greaterkashmir.com/latest/")
soup = BeautifulSoup(r.content, 'html5lib')
headings = soup.find_all('h2')
for h in headings:
    print(h.text)