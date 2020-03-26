import requests
import bs4
from bs4 import BeautifulSoup

# [1] WANNABE / ITZY

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.genie.co.kr/chart/top200?ditc=D&rtm=N&ymd=20200309',headers=headers)

soup = bs4.BeautifulSoup(data.text, 'html.parser')

aTags = soup.select('td.info > a.title.ellipsis')
for a in aTags:
    print(a.text)

