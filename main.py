# 단어 퍼즐 생성기 
import random
correct = 0 
wrong = 0

# 띄어쓰기를 기준으로 단어들 입력 
words = input().split() 

# 문제 랜덤으로 섞기 
for i in words : 
    ran_word = ''
    for r in random.sample(i, len(i)) : 
        ran_word += r
    # 문제 출력 
    print(f'문제: {"".join(ran_word)}')
    # 정답 입력 설정 
    input_value = input('정답 입력: ')
    if input_value == i :
        print('정답!')
        correct += 1
    else : 
        print('오답!')
        wrong += 1

# 종료 시 결과 출력 
print('게임 종료')
print(f'정답: {correct}개')
print(f'오답: {wrong}개')

    
