# 패스워드 변경서비스
members = {'aaa':'1111','bbb':'2222','ccc':'3333','ddd':'4444'}

print('패스워드 변경서비스입니다')
id = input('아이디를 입력하세요 : ')

if id not in members:
    print(f'입력하신 아이디 [{id}]는 존재하지 않습니다')
    print(f'패스워드 변경서비스를 종료합니다')
    exit(0)

password = input('현재패스워드를 입력하세요 : ')
if members.get(id) != password:
    print('패스워드가 일치하지 않습니다')
    print('서비스를 종료합니다')
    exit(0)

newPassword = input('변경할 패스워드를 입력하세요 : ')
members.update({id:newPassword})
# members.update(id=newPassword)  key가 변수명일때는 = 이 안먹히기 때문에 key=value 공식을 못씀
# members.update([id,newPassword]) 19번째줄과 21번째줄 2가지 방법이있음

print('<전체 회원 목록>')
print('아이디\t패스워드')
for id, pw in members.items():
    print(f'{id}\t\t{pw}')
