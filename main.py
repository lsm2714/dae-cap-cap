import random 

# 랜덤 숫자 선택 
random_num = random.choice(range(1, 101))

# 반복 설정 
count = 1
while True : 
    input_value = int(input('숫자를 맞춰보세요 (1~100): '))
    if input_value > random_num :
        print('DOWN!')
        count += 1
    elif input_value < random_num : 
        print('UP!')
        count += 1
    else : 
        print(f'정답입니다! 총 {count}회 만에 맞추셨습니다.')
        break
    

            
            
    




