
# 111
문자열 = input("문자열 입력 : ")
print(문자열*2)

# 112
숫자 = int(input("숫자 입력 : "))
print(숫자+10)

# 113
숫자 = int(input("숫자 입력 : "))
if 숫자%2 == 0 :
    print("짝수")
else :
    print("홀수")

# 114
숫자 = int(input("숫자 입력 : "))
if 숫자 + 20 > 255 :
    print(255)
else :
    print(숫자+20)

# 115
숫자 = int(input("숫자 입력 : "))
if 숫자 - 20 > 255 :
    print(255)
elif 숫자 - 20 < 0 :
    print(0)
else :
    print(숫자-20)

# 116
시간 = input("시간 입력 : ")
if 시간[3:5] == "00" :
    print("정각입니다.")
else :
    print("정각이 아닙니다.")

# 117
fruit = ["사과","포도","홍시"]
과일 = input("좋아하는 과일은? ")
if 과일 in fruit :
    print("정답입니다")
else :
    print("오답입니다")

# 118
warn_investment_list = ["Microsoft", "Google", "Naver", "Kakao", "SAMSUNG", "LG"]
투자종목 = input("투자 종목명 : ")
if 투자종목 in warn_investment_list :
    print("투자 경고 종목입니다")
else :
    print("투자 경고 종목이 아닙니다")

# 119
fruit = { "봄":"딸기" , "여름":"토마토" , "가을":"사과" }
계절 = input("좋아하는 계절은 : ")
if 계절 in fruit.keys() :
    print("정답입니다")
else :
    print("오답입니다")

# 120
fruit = { "봄":"딸기" , "여름":"토마토" , "가을":"사과" }
과일 = input("좋아하는 과일은 : ")
if 과일 in fruit.values() :
    print("정답입니다")
else :
    print("오답입니다")