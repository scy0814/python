'''
데이터를 입력하세요
10 5 23 89 11.2 5 16 8 'hello'  : 실수와 문자열은 무시
소수 출력
23 89

1단계
정수의 합 : (10 + 5 + 23 + 89 + 5 + 16 + 8)

2단계
소수출력 5 23 89 5

3단계
['',5,89,'',5,16,'','']
'''

num = 25
i = 2
while i < num and num % i :
    i += 1
    print('소수' if i == num else '비소수')

# data = input('데이터를 입력하세요').split()
# print(data)
# for numStr in data :
#     if numStr.isdigit():
#         num = int(numStr)