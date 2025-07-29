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

# 등급표 설정 
dict_value = {
    'A' : [i for i in range(90, 101)],
    'B' : [i for i in range(80, 90)],
    'C' : [i for i in range(70, 80)],
    'D' : [i for i in range(60, 70)],
    'F' : [i for i in range(0, 60)]
}

# 반복 설정 + 학생 정보 딕셔너리에 추가 
students = {}
while True : 
    name = input('학생의 이름을 입력하세요: ')
    if name == '종료' :
        break 
    number = int(input('학생의 점수를 입력하세요: '))
    students[name] = number 

if students == {} :
    print('입력된 학생 정보가 없습니다.')
else : 
    print('---- 결과 ----')
    for name, number in students.items() :
        print(f'{name}: {number}점', end='')
        for a in dict_value.keys() :
            if number in dict_value[a] :
                print(f' ({a}등급)')





