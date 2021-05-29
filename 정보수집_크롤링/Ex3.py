

from bs4 import BeautifulSoup as bs
import urllib.request as ur
import urllib

# 신촌날씨 온도 출력하기
지역 = input("지역:")
검색어 = urllib.parse.quote( 지역+'날씨' )

주소 = 'https://search.naver.com/search.naver?ie=utf8&query=' + 검색어

웹문서 = ur.urlopen( 주소 )
soup = bs( 웹문서.read() , 'html.parser')
온도 = soup.find_all('span', {'class': 'todaytemp'})
print("현재", 지역 + "의 날씨 :", 온도[0].text + "도")

# 미세먼지 출력
미세먼지 = soup.find_all('dd' , {"class":"lv1"})
print("현재", 지역 + "의 미세먼지:", 미세먼지[0].text)

# 오존지수 출력
오존지수 = soup.find_all("dd",{"class":"lv2"})
print("현재", 지역 + "의 오존지수:", 오존지수[0].text)