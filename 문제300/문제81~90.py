
# 081
scores = [8.8,8.9,8.7,9.2,9.3,9.7,9.9,9.5,7.8,9.4]
*valid_score, a,b = scores
print(valid_score)

# 082
scores = [8.8,8.9,8.7,9.2,9.3,9.7,9.9,9.5,7.8,9.4]
a,b,*valid_score = scores
print(valid_score)

# 083
scores = [8.8,8.9,8.7,9.2,9.3,9.7,9.9,9.5,7.8,9.4]
a,*valid_score,b = scores
print(valid_score)

# 084
temp = {}

# 085
icecream = { "메로나":1000 , "폴라포":1200 , "빵빠레":1800 }
print(icecream)

# 086
icecream["죠스바"] = 1200
icecream["월드콘"] = 1500
print(icecream)

# 087
print("메로나 :",icecream["메로나"])

# 088
icecream["메로나"] = 1300
print(icecream)

# 089
del icecream["메로나"]
print(icecream)

# 090
# 딕셔너리에 없는 키를 사용했기 때문