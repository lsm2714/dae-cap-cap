# 주사위 2개의 합 맞추기 
import random 

# 랜덤으로 생성한 주사위 값 2개 더하기 (중복 가능)
ran_number = []
for _ in range(2) : 
    ran = random.choice(range(1, 7)) 
    ran_number.append(ran)
ran_sum = sum(ran_number)

# 반복 설정 (5번 시도해도 오답일 시 빠져나가기)
count = 1
while count != 6 : 
    count += 1 # 이거 다섯 번째 시도에서 6 되는데 while 반복문은 while 반복문 밖의 코드를 기준으로 잡기 때문에
    # 전부 틀리고 아래 코드가 다 끝나야 밖의 count가 6이 되서 종료함 
    print('주사위 두 개의 합을 맞춰보세요! (2 ~ 12)')
    input_value = int(input('입력: '))
    if input_value != ran_sum :
        if count != 6 :
            print('틀렸습니다! 다시 시도하세요.')
    else : 
        print(f'정답입니다! 주사위: {", ".join([str(i) for i in ran_number])} (합: {ran_sum})')
        exit() 

print(f'게임 오버! 정답은 {ran_sum}였습니다.')
