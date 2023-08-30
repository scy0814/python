# 3 6 9 게임

import random
#1
num = random.randint(20, 50)
print(f'추출된 난수: {num}')

for i in range(1, num + 1):
    count = str(i).count('3') + str(i).count('6') + str(i).count('9')

    if count == 1:
        print('짝', end='\n')
    elif count == 2:
        print('짝짝', end='\n')
    elif i % 10 == 0:
        print((i // 10) * '뽀', '숑', end='\n')
    else:
        print(i, end='\n')

print()

#2
num = random.randint(20, 50)
print(f'추출된 난수: {num}')

print('<369게임 시작!!!>')
for i in range(1, num+1):

    n1 = i % 10
    n10 = i // 10

    print(f'{i:<3}', end=' ')
    if not n1:
        print('뽀'*n10,'숑', end='')
    if n1 in [3,6,9] :
        print('짝',end='')
    if n10 in [3,6,9]:
        print('짝',end='')

    print()




