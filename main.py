# 출석 관리 프로그램 
dict_value = {}

# 반복 설정 
while True : 
    select = int(input('''
==== 출석 관리 프로그램 ==== 
1. 학생 추가 
2. 학생 삭제
3. 출석 체크
4. 출석 현황 보기 
5. 종료
선택: '''))
    
    # 1번 선택 설정 
    if select == 1 :
        student_name = input('학생 이름: ')
        if student_name not in dict_value :
            dict_value[student_name] = '결석' 
            print(f'{student_name} 학생이 추가되었습니다!\n')
        else : 
            print('이미 있는 학생 이름입니다.\n')
    
    # 2번 선택 설정 
    elif select == 2 : 
        student_name = input('삭제할 학생 이름: ')
        if student_name in dict_value : 
            del dict_value[student_name] 
            print('학생 정보가 삭제되었습니다.\n')
        else : 
            print('해당 학생의 이름이 저장되어 있지 않습니다.\n')
    
    # 3번 선택 설정 
    elif select == 3 : 
        check = input('출석 체크할 학생 이름: ')
        if check in dict_value : 
            dict_value[check] = '출석'
            print(f'{check} 학생이 출석 처리되었습니다.\n')
        else : 
            print('해당 학생의 이름이 저장되어 있지 않습니다.\n')
    
    # 4번 선택 설정 
    elif select == 4 : 
        print('출석 현황: ')
        if dict_value != {} :
            for k, v in dict_value.items() : 
                print(f'- {k}: {v}')
            print()
        else : 
            print('저장된 학생 정보가 없습니다.\n')

    # 5번 선택 설정 
    elif select == 5 :
        break

    # 잘못된 입력 설정 
    else :
        print('잘못된 입력입니다. 1부터 5 사이의 숫자 중에서 선택해 주세요.\n')

print('프로그램을 종료합니다.')