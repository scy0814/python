members = {'홍길동':'1111-2222','박길동':'3333-4444','윤길동':'5555-6666'}

print(f'홍길동 존재여부: {"홍길동" in members}')
print(f'고길동 존재여부: {"고길동" in members}')
# print(f'3333-4444 존재여부: {"3333-4444" in members}')         #key에 대한 존재여부만 판단가능, value값은 판단 불가

print(members.keys())
print(members.values())
print(members.items())

for data in members:
    # print(data, end=' ')
    print(f'{data} : {members.get(data)}')
print()

for data in members.keys():   #이 방법이 훨씬 직관적
    print(data, end=' ')
print()

for data in members.values():
    print(data, end=' ')
print()

nums= [2, 3, 6]
a, b, c = nums    # a = nums[0], b = nums[1] c = nums[2]
print(f'a:{a}, b:{b}')
for key, value in members.items():
    print(f'{key}:{value}')

keys = ['name', 'age', 'addr']
mem = dict.fromkeys(keys,"")
print(mem)