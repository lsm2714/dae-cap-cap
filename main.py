# 구구단 출력기
list_value = [i for i in range(2, 10)]

# 단 입력받기 
gugudan = int(input('단을 입력하세요 (2단부터 9단까지): '))

if gugudan in list_value : 
    for i in list_value : 
        print(f'{gugudan} X {i} = {gugudan * i}')
else : 
    print('잘못된 입력입니다. 2단부터 9단까지 입력해 주세요.')
    

