import random 
numbers = ['첫', '두', '세']
word_list = []

# 단어 세 개 받기 
for i in numbers : 
    word = input(f'{i} 번째 단어를 입력하세요\n')
    if len(word) > 20 or len(word) < 5 : 
        while True :
            word = input('길이가 5 이상, 20 이하인 단어를 입력하세요\n')
            if len(word) < 20 and len(word) > 5 :
                break
    word_list.append(word)

# 랜덤으로 단어 선택 
ran = random.choice(word_list)
print(f'\n단어 선택 완료 게임을 시작합니다. 선택된 단어: {ran}')

# 선택된 단어의 50%(홀수일 경우 반올림)를 블라인드 처리 
index = [i for i in range(len(ran))]
if len(ran) % 2 == 0 :
    num = len(ran) / 2 
else : 
    num = len(ran) / 2 + 0.5 
    
blind_index = [i for i in random.sample(index, int(num))]

blinded = ['_' if i in blind_index else e for i, e in enumerate(ran)]

# 단어 맞추기 설정 (반복)
count = 1 
while '_' in blinded : 
    print(f'\n{count}번째 시도, 아래 단어를 구성하는 글자 한 개를 입력하세요')
    print(' '.join(blinded))
    guess = input() 
    count += 1
    if len(guess) != 1 :
        print(f'한 글자만 입력하세요.')
        continue
    
    # 맞출 경우 블라인드 제거 설정 
    if guess in ran : 
        hit = 0
        for i, e in enumerate(ran) : 
            if guess == e and blinded[i] == '_' :
                blinded[i] = guess 
                hit += 1 
        print(f'\n입력한 글자 단어 내 포함: {hit}글자')
    else : 
        print('\n단어 내 포함되지 않는 글자입니다.')

print(f'\nClear - 선택된 단어: {ran}, 총 시도 횟수: {count - 1}')

    

