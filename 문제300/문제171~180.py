
# 171
price_list = [32100,32150,32000,32500]
for i in range(4):
    print(price_list[i])

# 172
price_list = [32100,32150,32000,32500]
for i in range(4):
    print(i,price_list[i])

# 173
price_list = [32100,32150,32000,32500]
for i in range(4):
    print(3-i,price_list[i])

# 174
price_list = [32100,32150,32000,32500]
for i in range(1,4):
    print(i*10+90,price_list[i])

# 175
my_list = ["가","나","다","라"]
for i in range(3) :
    print(my_list[i], my_list[i+1])

# 176
my_list = ["가","나","다","라","마"]
for i in range(3) :
    print(my_list[i], my_list[i+1],my_list[i+2])

# 177
my_list = ["가","나","다","라"]
for i in range(1,4) :
    print(my_list[4-i], my_list[3-i])

# 178
my_list = [100,200,400,800]
for i in range(3) :
    print(my_list[i+1]-my_list[i])

# 179
my_list = [100,200,400,800,1000,1300]
for i in range(1,5) :
    print((my_list[i-1] + my_list[i] + my_list[i+1]) / 3)

# 180
volatility = []
low_prices = [100,200,400,800,1000]
high_prices = [150,300,430,880,1000]
for i in range(5) :
    volatility.append(high_prices[i] - low_prices[i])
print(volatility)