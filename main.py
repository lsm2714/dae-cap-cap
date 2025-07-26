number = int(input('숫자 입력 : '))

for i in range(1, number + 1) : 
    for _ in range(i) : 
        print('*', end='')
    print() 
for i in range(number - 1, 0, -1) : 
    for _ in range(i) : 
        print('*', end='')
    print() 
