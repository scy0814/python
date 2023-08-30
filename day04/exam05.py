#quit가 나올때까지 문자열을 입력받아test02.txt에 저장
# test02.txt에 저장된 모든 문자열 읽어서 모니터에 출력

# file = open('test.txt',"w") # 없으면 파일생성됨
# file.write('hello')
# file.close() # 다썼으면 닫아주기

# with open('test02.txt', "w") as file:
#     print('문자열들을 입력하세요. quit 입력시 종료')
#     while True:
#         msg = input()
#         if msg == 'quit':
#             break
#         # file.write('{0}\n'.format(msg))
#         file.write('{msg}\n')
#
# print('파일저장 완료...')

print('<읽어온 데이터>')

# 이 방법은 말이 안됨. 안에 몇 줄이 들어있을 줄 알고 ?
# with open('test02.txt','r') as file:
#     for i in range(3):
#         msg = file.read()
#         print(msg)

with open('test02.txt','r') as file:
    lines = file.readlines()

print('<읽어온 데이터 출력>')
for line in lines:
    print(line.rstrip('\n'))