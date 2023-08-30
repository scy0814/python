# set
data =set([1,2,3,4])
data2 = {1, 4, 5, 6}
print(type(data),data)
print(type(data2),data2)

print(f'합집합(data, data2) : {data.union(data2)}')    #union : 합집합 구하는 함수
print(f'합집합(data, data2) : {data | data2}')    # | : 합집합 연산자
print(f'교집합(data, data2) : {data.intersection(data2)}') #intersection : 교집합 구하는 함수
print(f'교집합(data, data2) : {data & data2}') # & : 교집합 연산자
print(f'차집합(data, data2) : {data.difference(data2)}') #difference : 차집합(data에서 교집합을 뺀 집합) 구하는 함수
print(f'차집합(data, data2) : {data - data2}') # - : 차집합(data에서 교집합을 뺀 집합) 연산자
print(f'대칭차집합(data, data2) : {data.symmetric_difference(data2)}') #symmetrice_difference : 대칭차집합(합집합에서 교집합을 뺀 집합) 구하는 함수
print(f'대칭차집합(data, data2) : {data ^ data2}') # ^ : 대칭차집합(합집합에서 교집합을 뺀 집합) 연산자
print(data,data2)