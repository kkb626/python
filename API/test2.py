
import os
import sys
import urllib.request
import json
import re

client_id = "GTTUYNwQquuE0mdKOvE3"
client_secret = "nzzwL5rJgv"

# 영화
검색어 = input("[영화]검색할 단어 :")
encText = urllib.parse.quote(검색어)
url = "https://openapi.naver.com/v1/search/movie?query=" + encText # json 결과
# url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText # xml 결과
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
response = urllib.request.urlopen(request)
rescode = response.getcode()
if(rescode==200):
    response_body = response.read()
    검색결과 = response_body.decode('utf-8')
    json결과 = json.loads(검색결과)
    for i in json결과['items'] :
        print(i['title'])
        print(i['director'])
        print(i['actor'])
        print(i['userRating'])
        break
else:
    print("Error Code:" + rescode)

# 책
검색어 = input("[책]검색할 단어 :")
encText = urllib.parse.quote(검색어)
url = "https://openapi.naver.com/v1/search/book?query=" + encText # json 결과
# url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText # xml 결과
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
response = urllib.request.urlopen(request)
rescode = response.getcode()
if(rescode==200):
    response_body = response.read()
    검색결과 = response_body.decode('utf-8')
    json결과 = json.loads(검색결과)
    for i in json결과['items'] :
        print(i['title'])
        print(i['author'])
        print(i['publisher'])
        break
else:
    print("Error Code:" + rescode)

# 쇼핑
검색어 = input("[쇼핑]검색할 단어 :")
encText = urllib.parse.quote(검색어)
url = "https://openapi.naver.com/v1/search/shop?query=" + encText # json 결과
# url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText # xml 결과
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
response = urllib.request.urlopen(request)
rescode = response.getcode()
if(rescode==200):
    response_body = response.read()
    검색결과 = response_body.decode('utf-8')
    json결과 = json.loads(검색결과)
    for i in json결과['items'] :
        print(i['title'])
        print(i['maker'])
        print(i['brand'])
        break
else:
    print("Error Code:" + rescode)