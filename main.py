# 숫자 퀴즈 게임 
import random
score = 0
numbers = [i for i in range(10)]

# 반복 설정 
while True : 
    select = int(input('''==== 숫자 퀴즈 게임 ====
1. 퀴즈 시작
2. 점수 보기
3. 종료
선택: '''))
    
    # 1번 선택 설정 
    if select == 1 :
        list_random = [i for i in random.sample(numbers, 2)]
        print(f'문제: {list_random[0]} + {list_random[1]} = ?')
        question = int(input('정답 입력: '))
        if question == sum(list_random) :
            score += 1
            print(f'정답입니다! 현재 점수: {score}점\n')
        else : 
            score -= 1
            print(f'오답입니다. 정답은 {sum(list_random)}입니다. 현재 점수: {score}점\n')
    
    # 2번 선택 설정 
    elif select == 2 :
        print(f'현재 점수: {score}\n')
    
    # 3번 선택 설정 
    elif select == 3 :
        break

    # 잘못된 입력 설정 
    else : 
        print('잘못된 입력입니다. 1부터 3 중에서 선택하세요.')
    
print(f'프로그램을 종료합니다. 최종 점수: {score}점')