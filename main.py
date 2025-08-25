# 콜라츠 추측 
# 숫자 입력 받기 
number = int(input('입력: ')) 
if number == 1 : 
    print('총 1단계 만에 1에 도달했습니다.')
else : 
    count = 0
    while number != 1 : 
        count += 1
        if number % 2 == 0 : 
            number /= 2 
        else :
            number = number * 3 + 1
    print(f'총 {count}단계 만에 1에 도달했습니다.') 
        
        



