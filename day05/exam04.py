class Dog:
    pass
dog = Dog()
print(type(dog))

class Car:
    def drive(self):
        print('운전을 합니다')

c = Car()
c.drive()
print(f'type(Car) 판단 : {isinstance(c, Car)}')
print(f'type(Car) 판단 : {isinstance(10, Car)}')
print(f'type(Car) 판단 : {isinstance([10, 20, 30], Car)}')

l = [10, 20, 30]
print(l[0],l.__getitem__(0))