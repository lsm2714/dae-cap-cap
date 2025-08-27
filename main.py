# 버스 요금 계산기 
list_value = []
ages1 = [i for i in range(8)]
ages2 = [i for i in range(8, 20)]
ages3 = [i for i in range(20, 65)]

# 반복 설정 
while True : 
    select = int(input('''==== 버스 요금 계산기 ====
1. 승객 추가
2. 승객 삭제
3. 승객 목록 보기
4. 총 요금 계산
5. 종료
선택: '''))
    
    # 1번 선택 설정 
    if select == 1 :
        name = input('이름: ')
        age = int(input('나이: '))
        if age in ages1 :
            money = 0
        elif age in ages2 :
            money = 1000
        elif age in ages3:
            money = 1500
        else : 
            money = 0
        list_value.append([name, age, money])
        if money != 0 :
            print(f'추가되었습니다! (요금: {money}원)\n')
        else : 
            print('추가되었습니다! (요금: 무료)\n')
    
    # 2번 선택 설정 
    elif select == 2 :
        index_list = []
        if list_value != [] :
            print('삭제할 고객의 인덱스를 선택해 주세요.')
            for i, e in enumerate(list_value) :
                print(f'{i}. {e[0]} ({e[1]}세)')
                index_list.append(i)
            index = int(input('인덱스 선택: '))
            if index in index_list :
                del list_value[index] 
                print('해당 승객 정보가 삭제되었습니다.\n')
            else : 
                print('인덱스 범위를 벗어났습니다.\n')
        else : 
            print('저장된 승객 정보가 없습니다.\n')
    
    # 3번 선택 설정 
    elif select == 3 : 
        if list_value != [] :
            print('승객 목록: ')
            for i in list_value : 
                print(f'- {i[0]} ({i[1]}세)')
            print() 
        else : 
            print('저장된 승객 정보가 없습니다.\n')
    
    # 4번 선택 설정 
    elif select == 4 :
        all_money = 0
        if list_value != [] :
            for i in list_value :
                all_money += i[2]
            print(f'총 요금: {all_money}원\n')
        else : 
            print('저장된 승객 정보가 없습니다.\n')
    
    # 5번 선택 설정 
    elif select == 5 :
        break
    
    # 잘못된 입력 설정 
    else : 
        print('잘못된 입력입니다. 1부터 5 사이의 선택지 중에서 선택해 주세요.\n')

print('프로그램이 종료되었습니다.')