# 단어 퀴즈 게임 만들기
import random
list_words = []
correct = 0
wrong = 0 
score = 0

# 딕셔너리에 퀴즈 단어 저장 + 단어만 따로 저장 
dict_value = {
    'おはようございます' : '안녕하세요',
    '権利' : '권리',
    '謙遜' : '겸손',
    '金融' : '금융',
    '霜' : '서리',
    '霧' : '안개',
    '相性' : '궁합이 맞음',
    'カラス' : '까마귀',
    'ひぐらし' : '쓰르라미'
}

for k in dict_value.keys() :
    list_words.append(k)

# 풀 문제의 개수 입력 
while True : 
    number = int(input('몇 문제를 푸시겠습니까? '))
    if number > len(dict_value) or number < 1 : 
        print('범위를 벗어났습니다.')
        continue
    else : 
        break

# 퀴즈 단어 출력 + 퀴즈 풀이 
count = 1
for i in random.sample(list_words, number) : 
    quiz = input(f'문제 {count}: {i}의 뜻은? -> ')
    # 정답일 경우
    if quiz == dict_value[i] :
        print('정답입니다!\n')
        correct += 1
        score += 10
    # 오답일 경우 
    else : 
        print(f'오답입니다. 정답: {dict_value[i]}\n')
        wrong += 1
    count += 1

# result 설정 
if correct / 2 < wrong : 
    result = '더 노력하세요!'
elif correct / 2 > wrong :
    result = '훌륭합니다!'
else : 
    result = '잘했어요!'

# 결과 출력 
print('=== 결과 ===')
print(f'정답 개수: {correct}')
print(f'오답 개수: {wrong}')
print(f'점수: {score}')
print(f'{result}')