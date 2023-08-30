def print_book(title, writer, price):
    print(f'제목 : {title}')
    print(f'글쓴이 : {writer}')
    print(f'가격 : {price}')
    pass

print_book('홍길동전','허균',15000)
print_book(title='홍길동전', writer='허균',price=15000)
print_book(price=15000,writer='허균', title='홍길동전')  #순서를 바꿔 써도 그대로 나옴

book = {'title':'홍길동전','writer':'허균','price':15000}

print_book(**book)