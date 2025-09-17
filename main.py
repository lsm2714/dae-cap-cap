# 가계부 관리 프로그램 
list_value = []
list_value_2 = []
dict_value = {}
money = 0

# 반복 설정
while True : 
    # (항목 이름, 금액, 카테고리)의 형태로 지출 입력
    input_value = input('지출 입력 (quit 입력 시 종료): ')
    if input_value == 'quit' : 
        break
    list_value.append(input_value)

# list_value의 안에 있는 요소들을 리스트로 변환 후 list_value_2에 집어넣기 
for e in list_value : 
    e = e.split(', ')
    list_value_2.append(e)

# 딕셔너리에 {카테고리 : 가격}의 형태로 저장
for i in list_value_2 : 
    if i[2] not in dict_value :
        dict_value[i[2]] = int(i[1])
    else : 
        dict_value[i[2]] += int(i[1])

# 지출 내역 출력 + 전체 지출 출력 
print('\n지출 내역: ')
for i in list_value_2 : 
    money += int(i[1])
    print(f'- {i[0]}: {i[1]}원 ({i[2]})')
    
print(f'\n전체 지출: {money:,}원')

# 카테고리별 지출 출력 
print('\n카테고리별 지출: ')
for k, v in dict_value.items() :
    print(f'{k}: {v:,}원')
