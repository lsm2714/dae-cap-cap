import random 

# 3개의 난수 생성 
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
computer = random.sample(numbers, 3)
print(computer)
# 반복 설정 
count = 1 
while True : 
    input_value = input(f'시도 {count}: 입력한 숫자 - ')
    num = input_value.split()
    num = [int(i) for i in num]
    # Strike, Ball, Out 판정 설정 
    st = 0
    ball = 0
    out = 0
    for i in range(3) : 
        if num[i] == computer[i] :
            st += 1 
        elif num[i] in computer : 
            ball += 1
        else : 
            out += 1
    print(f'결과: {st} Strike, {ball} Ball', end='')
    if out >= 1 :
        print(f', {out} Out')
    else : 
        print()
    
    count += 1
    
    # 승리, 패배 조건 설정 
    if st == 3 :
        print(f'게임 종료: 승리\n정답: ', end='')
        for i in computer :
            print(i, end=' ')
        print()
        break
    elif out == 3 : 
        print(f'게임 종료: 패배\n정답: ', end='')
        for i in computer :
            print(i, end=' ')
        print()
        break
    if count == 6 :
        print(f'게임 종료: 패배 (시도 횟수 5회 초과)\n정답: ', end='')
        for i in computer :
            print(i, end=' ')
        print()
        break
    


            
            
    




