data = [10, 20, 30, 40, 'hello']
print(type(data), data)
data = list()
print(type(data),data)

data = (10, 20, 30, 40)
print(type(data), data)
data = tuple()
print(type(data), data)

#data = 10
data = 10, 20 #임의의 값을 ,를 사용해서 넣으면 tuple로 인식함
print(type(data), data)

data = range(10) #range(10)은 0부터 10개의 숫자를 만들겠다는 의미 시작 숫자를 입력하지 않아 디폴트로 0값을 가짐
print(type(data), data)
data = list(data)
print(data)

data = range(5, 15) #시작숫자 5를 입력하고 종료값 15를 입력해서 5로 시작해서 15까지의 숫자를 가짐 단 step값을 입력하지 않아 디폴트 값으로 1씩 증가함
print(list(data))

data = list(range(1, 10, 2)) #시작값 종료값 스텝값을 모두 입력해서 1에서 시작해서 10이 될때까지 2씩 증가하는 숫자를 가짐
print(data)

data = list(range(20, 4, -3))
print(data)

data = list(range(20, 4, -3))
print(data)
print(16 in data, 17 in data) #16과 17이 data값 안에 있는지 없는지 True False로 확인
print('elo' in 'Hello')
print(4 in range(10)) #range(10) 안에 4가 있는지 없는지 True False로 확인