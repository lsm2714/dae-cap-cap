# 피라미드 출력기
# 정수 입력받기 
number = int(input('정수를 입력하세요: '))

# 피라미드 출력하기 
for num in range(1, number + 1) : 
    for _ in range(number - num) : 
        print(' ', end=' ')
    for _ in range(num) : 
        print('*', end=' ')
    for _ in range(num - 1) :
        print('*', end=' ')
    print()
    

        
        



