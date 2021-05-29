

from bs4 import BeautifulSoup as bs
import urllib.request as ur
import urllib

# 자동차 모델명 입력을 받아 출시가 크롤링

while True : # 무한 입력받기
    모델명 = input("자동차 모델명 :")
    검색어 = urllib.parse.quote(모델명)

    주소 = 'https://search.naver.com/search.naver?ie=utf8&query=' + 검색어
    웹문서 = ur.urlopen(주소)
    soup = bs( 웹문서.read(), 'html.parser')
    가격 = soup.find_all("span", {"class":""})
    찾는문자 = "판매" # 판매 포함된 문자 찾기

    for i in 가격 :
        b = 찾는문자 in i.text # 만약에 가격에 판매가 포함되어 있으면
        if b : # 출력
            print("현재 모델의 출시가 :" , i.text)
            # 아니면 출력X
