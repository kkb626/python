
# 121
문자 = input("문자 : ")
if 문자.islower() == True :
    print(문자.upper())
else :
    print(문자.lower())

# 122
점수 = int(input("점수 : "))
if 81<=점수<=100 :
    print("학점 : A")
elif 61<=점수<=80:
    print("학점 : B")
elif 41<=점수<=60 :
    print("학점 : C")
elif 21<=점수<=40 :
    print("학점 : D")
else :
    print("학점 : E")

# 123
환율 = { "달러":1167, "엔":1.096, "유로":1268, "위안":171}
입력 = input("환율&통화명 :")
금액, 통화명 = 입력.split()
print(float(금액) * 환율[통화명], "원")

# 124
정수1 = int(input("정수1 :"))
정수2 = int(input("정수2 :"))
정수3 = int(input("정수3 :"))
if 정수1>정수2 and 정수1>정수3 :
    print(정수1)
elif 정수2>정수1 and 정수2>정수3 :
    print(정수2)
else :
    print(정수3)

# 125
번호 = input("전화번호 :")
if 번호[:3] == "011" :
    print("통신사 : SKT")
elif 번호[:3] == "016" :
    print("통신사 : KT")
elif 번호[:3] == "019" :
    print("통신사 : LGU")
elif 번호[:3] == "010" :
    print("통신사 알 수 없음")

# 126
우편번호 = input("우편번호 :")
if 우편번호[:3] == "010" or 우편번호[:3] == "011" or 우편번호[:3] == "012" :
    print("강북구")
elif 우편번호[:3] == "013" or 우편번호[:3] == "014" or 우편번호[:3] == "015" :
    print("도봉구")
elif 우편번호[:3] == "016" or 우편번호[:3] == "017" or 우편번호[:3] == "018" or 우편번호[:3] == "019" :
    print("노원구")

# 127
주민등록번호 = input("주민등록번호 :")
if 주민등록번호[7] == "1" or 주민등록번호[7] == "3" :
    print("남자")
else :
    print("여자")

# 128
주민등록번호 = input("주민등록번호 :")
뒷자리 = 주민등록번호.split("-")[1]
if 0 <= int(뒷자리) <= 8 :
    print("서울입니다")
else :
    print("서울이 아닙니다")

129
주민등록번호 = input("주민등록번호 :")
계산 = (int(주민등록번호[0])*2 + int(주민등록번호[1])*3 + int(주민등록번호[2])*4 + int(주민등록번호[3])*5 + \
     int(주민등록번호[4])*6 + int(주민등록번호[5])*7 + int(주민등록번호[7])*8 + int(주민등록번호[8])*9 + \
     int(주민등록번호[9])*2 + int(주민등록번호[10])*3 + int(주민등록번호[11])*4 + int(주민등록번호[12])*5)%11
계산2 = 11-계산
if 주민등록번호[13] == 계산2 :
    print("유효한 주민등록번호입니다.")
else :
    print("유효하지 않은 주민등록번호입니다.")

# 130
import requests
btc = requests.get("https://api.bithumb.com/public/ticker/").json()['data']
변동폭 = float(btc['max_price']) - float(btc['min_price'])
시가 = float(btc['opening_price'])
최고가 = float(btc['max_price'])
if (변동폭 + 시가) > 최고가 :
    print("상승장")
else :
    print("하락장")