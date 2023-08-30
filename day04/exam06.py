print('<읽어온 데이터>')

#방법 2
with open('test02.txt', 'r') as file:
    for line in file:
        print(line.rstrip('\n'))


    #     line = file.readline().rstrip('\n')
    # line = None
    # while line != '':
    #     line = file.readline().rstrip('\n')
    #     print(line)




#방법 1
# with open('test02.txt', 'r') as file:
#     while True:
#         line = file.readline()
#         if line =='':
#             break
#         print('[{}]'.format(line.rstrip("\n")))

