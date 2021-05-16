
# 211
# 안녕
# Hi

# 212
# 7
# 15

# 213
# 정의한 함수와 다르게 실행할 때 괄호 안에 문자열을 넣지 않았기 때문이다.

# 214
# 문자열과 정수는 더할 수 없기 때문이다.

# 215
def print_with_smile(문자열) :
    print(문자열 + ":D")

# 216
print_with_smile("안녕하세요")

# 217
def print_upper_price() :
    현재가격 = int(input("현재가격 :"))
    print("상한가 :" , 현재가격*1.3)

print_upper_price()

# 218
def print_sum() :
    정수1 = int(input("정수1 :"))
    정수2 = int(input("정수2 :"))
    print(정수1 + 정수2)

print_sum()

# 219
def print_arithmetic_operation() :
    정수1 = int(input("정수1 :"))
    정수2 = int(input("정수2 :"))
    print(정수1, "+", 정수2, "=", 정수1 + 정수2)
    print(정수1, "-", 정수2, "=", 정수1 - 정수2)
    print(정수1, "*", 정수2, "=", 정수1 * 정수2)
    print(정수1, "/", 정수2, "=", 정수1 / 정수2)
print_arithmetic_operation()

# 220
def print_max() :
    정수1 = int(input("정수1 :"))
    정수2 = int(input("정수2 :"))
    정수3 = int(input("정수3 :"))
    if 정수1 > 정수2 and 정수1 > 정수3 :
        print(정수1)
    elif 정수2 > 정수1 and 정수2 > 정수3 :
        print(정수2)
    else :
        print(정수3)
print_max()