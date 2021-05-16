
# 191
data = [ [2000,3050,2050,1980] , [7500,2050,2050,1980] , [15450,15050,15550,14900] ]
for 열 in data :
    for 행 in 열 :
        print( 행*1.00014 )

# 192
data = [ [2000,3050,2050,1980] , [7500,2050,2050,1980] , [15450,15050,15550,14900] ]
for 열 in data :
    for 행 in 열 :
        print( 행*1.00014 )
    print("----")

# 193
result = []
for 열 in data :
    for 행 in 열 :
        result.append( 행*1.00014 )
print(result)

# 194
result = []
for 열 in data :
    계산 = []
    for 행 in 열 :
        계산.append(행*1.00014)
    result.append(계산)
print(result)

# 195
ohcl = [ ["open","high","low","close"], [100,110,70,100], [200,210,180,190], [300,310,300,310] ]
for 열 in ohcl[1:] :
    print(열[3])

# 196
ohcl = [ ["open","high","low","close"], [100,110,70,100], [200,210,180,190], [300,310,300,310] ]
for 열 in ohcl[1:] :
    if 열[3] > 150 :
        print(열[3])

# 197
ohcl = [ ["open","high","low","close"], [100,110,70,100], [200,210,180,190], [300,310,300,310] ]
for 열 in ohcl[1:] :
    if 열[3] >= 열[0] :
        print(열[3])

# 198
volatility = []
ohcl = [ ["open","high","low","close"], [100,110,70,100], [200,210,180,190], [300,310,300,310] ]
for 열 in ohcl[1:] :
    volatility.append(열[1] - 열[2])
print(volatility)

# 199
ohcl = [ ["open","high","low","close"], [100,110,70,100], [200,210,180,190], [300,310,300,310] ]
for 열 in ohcl[1:] :
    if 열[3] > 열[0] :
        print(열[1] - 열[2])

# 200
수익 = []
ohcl = [ ["open","high","low","close"], [100,110,70,100], [200,210,180,190], [300,310,300,310] ]
for 열 in ohcl[1:] :
    수익.append(열[3] - 열[0])
print(sum(수익))