# 단어 섞기 퀴즈 
import random 

# 단어 목록 준비 
words = ['크리치비치', '자바스크립트', '야이여자야', '케모노프렌즈']

# 특정 단어 선택 후 랜덤으로 섞기 (랜덤으로 섞은 단어는 원래 형태와 같아선 안됨)
word = random.choice(words)
word_list = [i for i in word]
# 같지 않은 게 나올 때까지 while 반복문 작동 
while True : 
    list_value = []
    for i in random.sample(word_list, len(word_list)) : 
        list_value.append(i)
    if word_list != list_value :
        break 

# 문제 출력, 입력, 결과 확인
ran_word = ''.join(list_value)
print(f'섞인 단어: {ran_word}')
guess = input('원래 단어는? ')
if guess == word :
    print('정답입니다!')
else : 
    print(f'오답입니다. 정답은 {word}였습니다.')
