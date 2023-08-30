# 정수 2개 입력받아 최대공약수 출력

num1, num2 = map(int, input('두개의 정수를 입력 : ').split())
print(num1,num2)

divNum = [i for i in range(1,num1+1) if num1 % i == 0]
divNum2 = [i for i in range(1, num2+1) if num2%i == 0]

divisor = [n for n in divNum if n in divNum2]

print(f'{num1} 약수들의 집합 : {divNum}')
print(f'{num2} 약수들의 집합 : {divNum2}')
print(divisor)
print(f'최대공약수 : {max(divisor)}')
print(f'최대공약수 : {max(set(divNum) & set(divNum2))}')
