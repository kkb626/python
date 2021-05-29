

from bs4 import BeautifulSoup as bs # html 언어 읽어주는 함수 제공
import urllib.request as ur
    # URL : 인터넷 주소 : www.naver.com

#1. 크롤링 할 인터넷주소 넣어주기
주소 = 'https://movie.naver.com/movie/running/current.nhn'

#2. 주소 열어서 웹문서 변수에 저장
웹문서 = ur.urlopen(주소)

#3. 웹문서 변수 읽기
soup = bs(웹문서.read() , 'html.parser')

#4. 해당태그를 찾아서 가져오기
태그 = soup.find_all('ul',{"class":"lst_detail_t1"})

print(태그)

# 영화 랭킹 크롤링하기
주소 = 'https://movie.naver.com/movie/sdb/rank/rmovie.nhn'
웹문서 = ur.urlopen(주소)
soup = bs(웹문서.read() , 'html.parser')
태그 = soup.find_all('div',{"class":"tit3"})
print(태그)