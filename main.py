'''import random
list_value = ['가위', '바위', '보']

# 가위 바위 보 입력 + 잘못된 입력일 경우 다시 입력 
while True : 
    input_value = input('가위/바위/보 중 하나를 입력하세요: ')
    if input_value not in list_value :
        print('잘못된 입력입니다. 가위, 바위, 보 중에서 하나를 입력하세요')
    else :
        break

# 컴퓨터가 랜덤으로 가위, 바위, 보 중 하나 선택 설정 
computer = random.choice(list_value)
print(f'컴퓨터의 선택: {computer}')

# 조건 설정 
rule = {
    '가위' : '보',
    '보' : '바위',
    '바위' : '가위'
}

if input_value == computer :
    result = '무승부!'
elif rule[input_value] == computer :
    result = '승리!'
else : 
    result = '패배!'
        
print(f'결과 : {result}')'''

# 과일 메뉴 딕셔너리 설정 
menu = {
    '사과' : 1000,
    '바나나' : 500,
    '딸기' : 1200
}

# 과일 이름 입력 + 개수 입력 등등 
menu_list = ['사과', '바나나', '딸기']
while True :
    name_value = input('과일 이름을 입력하세요: ')
    if name_value in menu_list :
        break
    else : 
        print('잘못된 입력입니다. 사과, 바나나, 딸기 중에서 입력하세요')

num = int(input('수량을 입력하세요: '))

print(f'총 가격은 {menu[name_value] * num}원입니다.')




