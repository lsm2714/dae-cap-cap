# ATM 프로그램 

# 반복문 안에 선택 설정하기 
money = 0 
while True : 
    # 메뉴 선택 설정 
    select = int(input('''==== ATM 프로그램 ====
1. 입금
2. 출금
3. 잔액 조회
4. 종료
선택: '''))
    
    # 1번 선택 설정 
    if select == 1 : 
        input_value_1 = int(input('입금 금액: '))
        money += input_value_1
        print(f'현재 잔액: {money}원\n')
        
    # 2번 선택 설정 
    elif select == 2 : 
        input_value_2 = int(input('출금 금액: '))
        if input_value_2 > money :
            print('잔액 부족!\n')
        else :
            money -= input_value_2
            print(f'출금 완료! 현재 잔액: {money}원\n')
            
    # 3번 선택 설정 
    elif select == 3 : 
        print(f'현재 잔액: {money}원\n')
        
    # 잘못된 입력 설정 
    elif select > 4 or select < 1 : 
        print('잘못된 입력입니다!\n')
        
    # 4번 선택 설정 
    else : 
        break
        
print('프로그램을 종료합니다.')