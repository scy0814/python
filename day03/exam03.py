'''
setdefault   : 새 데이터 삽입
update       : key 없으면 데이터 삽입, key 없으면 데이터 수정
pop          : 데이터 삭제
'''

members = {'홍길동':'010-1111-2222','박길동':'010-3333-4444'}
print(members)
members.setdefault('윤길동','010-5555-6666')
members.setdefault('이길동')
print(members)
# members.setdefault('이길동','010-7777-8888') 새 데이터 삽입 O, 기존데이터 수정 X
members.update(이길동='010-7777-8888')
members.update(한길동='010-9999-0000')
members.update({20340501:'010-2345-6789'})    #update는 문자열만 가능해서 dict으로 정수를 추가
members.update([[20240502,'010-1234-5678'],['고길동','010-4567-8901']])
members.update(zip(['park','이길동'],['8282',None]))
print(members)

value = members.pop('이길동')
print(f'pop("이길동" : {value}')
members.pop('구길동',"없음")
print(members)

members.popitem()
print(members)

value = members.get('홍길동')
print(f'홍길동 : {value}')
print(f'이길동 : {members.get("이길동","존재하지 않음")}')