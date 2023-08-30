'''
    list 내장함수
    append : 데이터 추가 (맨마지막)
    insert : 데이터 추가 (특정위치)

    pop    :데이터 삭제 (맨마지막) 인덱스 쓸 수 있음
    remove :데이터 삭제 (특정위치)

    index  : 특정값 위치 검색
    count  : 특정값의 빈도수
    reverse: 위치 뒤집기
    sort   : 정렬
    clear  : 리스트 요소 전부 삭제


    stack LIFO
    queue FIFO
'''

data = []
print(data, id(data))
data.append(10)
data.append(20)
data.append(30)
print(data, id(data))
delData= data.pop()  # 스택처럼 만든 방식   append랑 pop이랑 같이 써야함
print('삭제된 값: ',delData)

data = list()
data.insert(0, 10)
data.insert(0, 20)
data.insert(0, 30) # 스택처럼 만든 방식
print(data, id(data))
delData=data.pop()
print('삭제된 값: ',delData)

# 큐처럼 쓸 때
data=[]
data.append(10)
data.append(20)
data.append(30)
print(data,id(data))
delData = data.pop(0)
print('삭제된 값: ',delData)

data=[10,20,30,40,30]
idx = data.index(30) # 여러번 있으면 맨 처음? 앞쪽에 있는애 가 나옴
cnt = data.count(30)
print('위치: ',idx)
print('개수: ',cnt)
print('before: ',data)
data.remove(30)
print('after: ',data)

for i in range(len(data)):
    print(data[i], end=' ')
print()

data =[10, 40, 20, 70, 50, 60, 30, 50]

sortData = sorted(data)
maximum = sortData[-1]
minimum = sortData[0]

# maximum = data[0]
# minimum = data[0]
# for d in data:
#     if minimum > d :
#         minimum = d
#     if maximum < d :
#         maximum = d


# ite = iter(data)
# print(next(ite))
# print(next(ite))
# print(next(ite))
# print(next(ite))
# print(next(ite))

data.reverse()
for d in iter(data):
    print(d, end=' ')
print()

for index, d in enumerate(data, start=100):
    print(f'[{index}] : {d}')

# print(data[-1])
# print(data[-2])
data.reverse()

# data2=reversed(data)
# print('data: ',data)
# print('data2: ',next(data2))

for d in reversed(data):
    print(d, end=' ')
print()

# data.sort()
# print(data)

print(sorted(data)) #reversed =False(default, 오름차순) =True(내림차순)
print(data)

data=[10, 20 ,30]
# for i in range(len(data)):
#     # data.pop(0)
# data.clear()
del data[:]
print(data)

