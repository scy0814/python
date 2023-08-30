'''
    input.txt 읽어 다음의 결과를 출력하시오
    1.총 단어의 개수 세어보기
    2.단어의 빈도수(알파벳순으로 출력)
    ex) a 15    abvoe : 1
        b 2
    3.단어가 몇번째 라인에 나왔는지 출력
'''

with open('input.txt', 'r') as file:
    line = file.readline().split()
    while line != '':
        print(line)
        line = file.readline().rstrip('\n')
        