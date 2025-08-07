import random 

numbers = ['첫 ', '두 ', '세 ']
words_list = []

# 반복 설정 
for i in numbers :
    word = input(f'{i}번째 글자를 입력하세요: ')
    if 5 > len(word) or len(word) > 20 :
        while True : 
            word = input('5 이상 20 이하 길이의 글자를 입력하세요\n')
            if 5 < len(word) and len(word) < 20 :
                break
    words_list.append(word)

ran = random.choice(words_list) 
print(f'\n단어 선택 완료 게임을 시작합니다. 선택된 단어: {ran}')

# 선택된 글자의 50% 가리기 
index = [i for i in range(len(ran))]
if len(ran) % 2 == 0 : 
    index_50 = len(ran) / 2
else : 
    index_50 = len(ran) / 2 + 0.5 
# 랜덤으로 블라인드 처리될 인덱스 가지기 
blind = [] 
for i in random.sample(index, int(index_50)) : 
    blind.append(i)
# 블라인드 처리 
blinded = ['_' if i in blind else v for i, v in enumerate(ran)]

# 글자 입력해서 블라인드 제거하기 
count = 1 
while '_' in blinded : 
    print(f'\n{count}번째 시도, 아래 문자를 구성하는 글자 1개를 입력하세요')
    print(' '.join(blinded))
    guess = input() 
    count += 1
    
    if len(guess) != 1 :
        print('한글자만 입력하세요')
        continue
    
    if guess in ran : 
        hit = 0
        for i in range(len(ran)) : 
            if guess == ran[i] and blinded[i] == '_': 
                blinded[i] = guess
                hit += 1 
        print(f'입력한 글자 블라인드 문자 내 포함: {hit}글자')
    else : 
        print('단어 내 포함되지 않는 글자입니다.')

# 결과 출력 
print(f'Clear - 선택된 단어: {ran}, 총 시도 횟수: {count - 1}')
    
    
            
    


    

    



            
            
    




