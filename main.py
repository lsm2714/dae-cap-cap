# 할 일 관리 프로그램 
list_value = []

# 반복 설정 
while True : 
    select = int(input('''==== 할 일 관리 프로그램 ====
1. 할 일 추가
2. 할 일 완료 처리
3. 할 일 삭제
4. 할 일 목록 보기
5. 종료
선택: '''))
    
    # 인덱스 리스트
    index_list = []
    for i, e in enumerate(list_value) :
        index_list.append(i)
    
    # 1번 선택 설정 
    if select == 1 : 
        input_value = input('할 일 내용: ')
        count = False 
        for i in list_value :
            if input_value == i[0] :
                count = True 
        if count == False :
            list_value.append([input_value, '미완료'])
            print('추가되었습니다!\n')
        else : 
            print('이미 저장된 할(한) 일입니다.\n')
    
    # 2번 선택 설정 
    elif select == 2 : 
        index = int(input('완료 처리할 인덱스: '))
        if index in index_list :
            list_value[index][1] = '완료'
            print(f'{list_value[index][0]} -> 완료 처리되었습니다!\n')
        else : 
            print('인덱스 범위를 벗어났습니다.\n')

    # 3번 선택 설정 
    elif select == 3 :
        index = int(input('삭제할 인덱스: '))
        if index in index_list :
            del list_value[index]
            print('삭제가 완료되었습니다.\n')
        else : 
            print('인덱스 범위를 벗어났습니다.\n')
    
    # 4번 선택 설정 
    elif select == 4 : 
        print('현재 할 일 목록: ')
        if list_value != [] :
            for i, e in enumerate(list_value) :
                print(f'{i}. [{e[1]}] {e[0]}')
            print()
        else : 
            print('할 일 목록이 없습니다.\n')

    # 5번 종료 설정 
    elif select == 5 :
        break

    # 잘못된 입력 설정 
    else :
        print('잘못된 입력입니다. 1부터 5 사이의 값 중 입력해 주세요.\n')

print('프로그램을 종료합니다.')