class Car:
    # def __init__(self,**args):
    #     for key, value in args.items():
    #         print(f'{key}:{value}')
    #     # self.args
    # def info(self):
    #     print(f'자동차명 : {self.name} \t 가격: {self.price}')
    #
    # pass
    addr = '서울'
    __slots__=['name','price','company']
    def __init__(self,**args):
        if 'name' in args:
            # self.add(value) #이런식으로 넣을 수 없음 의미가없다...
            self.name=args['name']
        if 'price' in args:
            self.price = args.get('price')
        if 'company' in args:
            self.company = args.get('company')
            Car.addr='부산'
        # self.args
    def info(self):

        print(f'자동차명 : {self.name} \t 가격: {self.price} \t 회사: ' )

    pass

c=Car(name='그랜저',price=4000, company='현대')
c2=Car(name='모닝',price=2100)

c.info()
c2.info()
print(c.addr)
print(c2.addr)