# ATM 출금 시뮬레이션 
dict_value = {} 
moneys = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
amounts = []

# 돈 입력받기 
amount = int(input('Enter amount: '))

# 10원 미만 출금 불가 설정 
while True : 
    if amount < 10 :
        print('10원 미만은 출금할 수 없습니다. 다시 입력해 주세요')
        continue
    else : 
        break
    
# 돈 출금 반복 설정 
for m in moneys : 
    # 빼는 돈이 바뀌 때마다 count 초기화
    count = 0 
    # amount가 m(돈)과 같거나 클 때만 계산 시작 
    while amount >= m : 
        amount -= m 
        count += 1
    # 딕셔너리에 집어넣기, amouts 리스트에 현재 남은 가격 집어넣기
    if count != 0 :
        # 쉼표 붙이기 
        if m >= 1000 :
            hit = 0
            m2 = str(m)
            m = ''
            for i in m2[::-1] : 
                hit += 1
                m += i
                if hit == 3 :
                    m += ','
            m = m[::-1]
        dict_value[f'{m}원'] = count
        amounts.append(amount)

# 결과 출력 
for k, v in dict_value.items() : 
    # 장, 개 구분
    if len(k) > 4 : 
        print(f'{k}: {v}장', end=' ')
    else : 
        print(f'{k}: {v}개', end=' ')
    print(f'(나머지: {amounts.pop(0)}원)')

    
