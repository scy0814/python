data = list(range(1,10))
print(data)

data2 = data[0:5]
print(data)
print(data2)
print(data[5:8]) #5번지부터 8번지 전까지
print(data[:3]) #처음 번지부터 3번지 전까지
print(data[3:]) #print(data[3:len(data)])
print(data[:]) #전부 다 찍는거

print(data)
#data2 = data #shallow copy
data2 = data[:] #Deep copy
print(data2)
data2[0] = 100
print('data : ', data, id(data))
print('data2 : ',data2, id(data2))

print(data[5:len(data)])
print(data[5:-1]) #print(data[5:len(data) -1])
#리스트명[시작 = 0:종료 = len(리스트):간격 = 1)
print(data[2:8:2])
print(data[2::2])
print(data[8:2:-2])
print(data[::-1])

print('data : ', data)


# data[2:5] = [100, 200, 300]
# print('data : ', data)
# data[2:5] = [100, 200, 300, 400, 500]
data[2:6:2] = [10, 20]
print('data : ', data)

# del data[2:3]
del data[2:5]
print('data : ', data)







