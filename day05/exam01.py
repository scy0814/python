print('abc')
print(10)
print([1,2,3,4,5],[10,20,30,40])
print(10,20,30,40,'aaa',end='\n',sep='')

def myPrint(*values,end='>'): #  values 가변인자(몇개가 들어올 지 모름), end는 뒤에 찍겠다 하는 구분인자 . end라는 인자를 안넘겨주면 default가 엔터, sep은 space
    for value in values:
        print(value, end=end)


myPrint(10,end='\n')
myPrint(10,'A')
myPrint((10,20,30,40),[100,200,300,400])
print()



def calc(command, *args):
    s = 0 if command == 'add' else 1;
    for value in args :
        if command == 'add':
            s += value
        elif command == 'mul' :
            s *= value
    return s
    print('command : ',command)
    print('args : ',args)

print(calc('add',12,7))
print(calc('add',12,6,9))
# print(calc('add',12,[6,9,10]))   이렇게 값을 주면 계산을 어떻게 해야할까?
print(calc('mul',12,7))
print(calc('mul',1,2,3,4,5))