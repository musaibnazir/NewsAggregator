from django.shortcuts import render
import requests
from bs4 import BeautifulSoup

toi_r = requests.get("https://timesofindia.indiatimes.com/briefs")
toi_soup = BeautifulSoup(toi_r.content, 'html5lib')
toi_headings = toi_soup.find_all('h2')
toi_headings = toi_headings[0:11]
toi_news=[]

for h in toi_headings:
    toi_news.append(h.text)



ht_r = requests.get("https://www.hindustantimes.com/india-news/")
ht_soup = BeautifulSoup(ht_r.content, 'html5lib')
ht_headings = ht_soup.findAll("div", {"class":"headingfour"})
ht_headings = ht_headings[2:11]
ht_news = []

for n in ht_headings:
    ht_news.append(n.text)


gk_r = requests.get("https://www.greaterkashmir.com/latest/")
gk_soup = BeautifulSoup(gk_r.content, 'html5lib')
gk_headings = gk_soup.find_all('h2')
gk_headings = gk_headings[0:10]
gk_news=[]

for g in gk_headings:
    gk_news.append(g.text)


def index(req):
    return render(req,'news/index.html', {'toi_news':toi_news, 'ht_news': ht_news, 'gk_news': gk_news})
