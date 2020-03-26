# scraping / crawling
# 1. html 을 가져온다
# 2. html 에서 내가 필요한 정보를 찾아낸다
# 3. 갖는다

import requests
import bs4

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=pnt&date=20200303', headers=headers)

r = requests.get('https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=pnt&date=20200303')

soup = bs4.BeautifulSoup(r.text, 'html.parser')

aTags = soup.select('Div.tit5 a')
for a in aTags[:10]:
    print(a.text)

