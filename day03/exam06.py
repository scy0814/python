members = {'홍길동':'32거2345','고길동':'26소2756','윤길동':'89나2134'}

# 홍길동의 차량번호 검색
print(members.get('홍길동'))

# 차량번호 26소2756의 소유주 검색
mem = {value:key for key, value in members.items()}
print(mem.get('26소2756'))

data = [key for key, value in members.items() if value == '26소2756']
print(data[0])
# for key, value in members.items():
#     if value == '26소2756':
#         print(key)
