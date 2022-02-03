import requests
from bs4 import BeautifulSoup

r = requests.get("https://www.hindustantimes.com/india-news/")
soup = BeautifulSoup(r.content, 'html5lib')
newsDiv = soup.findAll("div", {"class":"headingfour"})
for n in newsDiv:
    print(n.text)