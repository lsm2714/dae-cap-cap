# 영화 예매 프로그램 
list_value = [[], [], [], [], []]
for i in list_value: 
    for _ in range(5) :
        i.append('O')

# 반복 설정 
while True : 
    select = int(input('''==== 영화 예매 프로그램 ====
1. 좌석 보기
2. 좌석 예매 
3. 좌석 취소
4. 종료
선택: '''))
    
    # 1번 선택 설정 
    if select == 1 :
        for i in list_value : 
            print(' '.join(i))
        print() 
    
    # 2번 선택 설정 
    elif select == 2 :
        rows = int(input('행 번호 입력 (1~5): '))
        columns = int(input('열 번호 입력 (1~5): '))
        if rows and columns in [1, 2, 3, 4, 5] :
            if list_value[rows - 1][columns - 1] == 'O' :
                list_value[rows - 1][columns - 1] = 'X'
                print('예매 완료!\n')
            else : 
                print('이미 예약된 좌석입니다.\n')
        else : 
            print('잘못된 입력입니다.\n')

    # 3번 선택 설정 
    elif select == 3 :
        rows = int(input('행 번호 입력 (1~5): '))
        columns = int(input('열 번호 입력 (1~5): '))
        if rows and columns in [1, 2, 3, 4, 5] :
            if list_value[rows - 1][columns - 1] == 'X' :
                list_value[rows - 1][columns - 1] = 'O'
                print('취소 완료!\n')
            else :
                print('예약되어 있는 자리가 아닙니다.\n')
        else : 
            print('잘못된 입력입니다.\n')
    
    # 4번 선택 설정 
    elif select == 4 : 
        break

    # 잘못된 입력 설정 
    else : 
        print('잘못된 입력입니다. 1부터 4 사이의 선택지 중에서 선택하세요.\n')

print('프로그램을 종료합니다.')

