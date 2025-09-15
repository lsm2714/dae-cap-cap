# 자판기 시뮬레이션 
moneys = [500, 100, 50, 10]
dict_money = {} 

dict_value = { # 메뉴
    '콜라' : 1200,
    '사이다' : 1000,
    '커피' : 1500,
    '물' : 700
} 

# 투입할 금액 입력 
money = int(input('투입 금액: '))

# 음료 구매 반복 설정 
while True : 
    name = input('구매할 음료: ')
    # '없음'일 경우 break
    if name == '없음' :
        break
    if name in dict_value : 
        # 만약 잔액이 충분할 경우 
        if dict_value[name] <= money :
            money -= dict_value[name]
            print(f'{name} 구매 완료')
        # 잔액 부족일 경우 
        else : 
            print('잔액 부족')
    # 잘못된 입력 설정
    else : 
        print('잘못된 입력입니다.')

# 잔돈 설정 (반복)
if money >= 10 :
    for m in moneys : 
        count = 0 # 동전 갯수 카운트
        # 빼기 반복 설정 
        while True : 
            if money < m : 
                break
            money -= m 
            count += 1
        # dict_money에 count가 0 이상인 것만 집어넣기 
        if count >= 1 :
            dict_money[f'{m}원'] = f'{count}개'
    # 잔돈 출력 설정 
    count = 0 
    print('잔돈: ', end='')
    for k, v in dict_money.items() :
        print(f'{k} {v}', end='') 
        # 쉼표 설정
        count += 1
        if count != len(dict_money) : 
            print(', ', end='')
else : 
    print('\n잔돈 없음')

    
