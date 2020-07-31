import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}

data = requests.get('https://www.genie.co.kr/chart/top200?ditc=D&rtm=N&ymd=20200713', headers=headers)
soup = BeautifulSoup(data.text, 'html.parser')
client = MongoClient('localhost', 27017)
db = client.dblank

trs = soup.select('#body-content .list-wrap > tbody > tr')

for tr in trs:
    rank = tr.select_one('.number').text[0:2].strip()
    title = tr.select_one('.title').text.strip()
    artist = tr.select_one('.artist').text

    list = {
        'rank': rank,
        'title': title,
        'artist': artist
    }
    
    db.genie.insert_one(list)