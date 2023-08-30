'''
quit이 나올때까지 정수를 입력받아 각 정수의 약수를 출력
10
6
36
87
23
40
quit
10의 약수 : [1, 2, 5, 10]
6의 약수 : [1, 2, 3, 6]
36의 약수 : [1, 2, 3, 4, 6, 9, 12, 18, 36]
    ...
40의 약수 : [1, 2, 4, 5, 8, 10, 20, 40]
'''

print('정수를 입력하시오. quit 입력시 종료됩니다')
inputs = list()
while True:
    data = input()
    if data.lower() == 'quit':
        break
    inputs.append(int(data))

for num in inputs:
    div = [i+1 for i in range(num) if num % (i+1) == 0]
    print(f'{num} 약수 : {div}')