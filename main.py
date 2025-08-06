# 가위, 바위, 보 확장 버전 (in, not in 연산자 사용 금지)
import random

count = 1 
win = 0
lose = 0 
draw = 0
list_value = ['가위', '바위', '보']

dict_value = {
    '가위' : '보',
    '바위' : '가위',
    '보' : '바위'
}

# 반복 설정 
while count < 4 : 
    input_value = input('\n가위, 바위, 보 중에서 하나를 입력하세요: ')
    if input_value != '가위' and input_value != '바위' and input_value != '보': 
        print('가위, 바위, 보 중에서 하나를 선택하세요.')
        continue
    computer = random.choice(list_value)
    print(f'파소콩의 선택: {computer}')
    if input_value == computer : 
        print('무승부!', end=' ')
        draw += 1 
    elif computer == dict_value[input_value] :
        print('승리!', end=' ')
        win += 1 
    else : 
        print('패배!', end=' ')
        lose += 1
    print(f'현재 전적: {win}승 {lose}패 {draw}무')
    count += 1

# 승패무 결과 설정 
print(f'전적: {win}승 {lose}패 {draw}무')
if win > lose :
    print('최종 승자: 이승민')
elif lose > win :
    print('최종 승자: 파소콩쨩')
else : 
    print('최종 결과: 무승부')
    



            
            
    




