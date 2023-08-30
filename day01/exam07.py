num = 1
while num <= 10 :
    print(num, end=' ')
    num += 1
print()

for i in range(10) :
    print(i+1, end=' ')

for i in range(10) :
    if (i+1) % 2:
        print(i+1, end=' ')
print()

for i in range(0, 10, 2):
    print(i+1, end=' ')
print()

names = ['홍길동','강길동','윤길동']
for name in names:
    print(name, end=' ')
print()
