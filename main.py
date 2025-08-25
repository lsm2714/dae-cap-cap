# 도서 관리 프로그램 만들기 
dict_value = {} 

# 반복 설정 
while True : 
    select = int(input(''' ==== 도서 관리 프로그램 ====
1. 책 추가
2. 책 삭제
3. 책 목록 보기 
4. 책 검색
5. 종료
선택: '''))
    
    # 1번 선택 설정 
    if select == 1 : 
        book_name = input('추가할 책 제목: ')
        lower_name = book_name.lower()
        if lower_name not in dict_value : 
            dict_value[lower_name] = 1
        else : 
            dict_value[lower_name] += 1
        print(f'추가되었습니다! (현재 권 수: {dict_value[lower_name]}권)\n')
        
    # 2번 선택 설정 
    elif select == 2 : 
        book_name = input('삭제할 책 제목: ')
        lower_name = book_name.lower()
        if lower_name not in dict_value : 
            print('저장되지 않은 책입니다.\n')
        else : 
            dict_value[lower_name] -= 1
            if dict_value[lower_name] == 0 :
                del dict_value[lower_name]
                print('해당 책의 마지막 권을 삭제했습니다. 목록에서 제거됩니다.\n')
            else : 
                print(f'1권 삭제되었습니다. (남은 권 수: {dict_value[lower_name]}권)\n')
    
    # 3번 선택 설정 
    elif select == 3 :
        print('현재 책 목록: ')
        if dict_value == {} : 
            print('저장되어 있는 책이 없습니다.\n')
        else : 
            for k, v in dict_value.items() :
                print(f'- {k} {v}권')
            print() 
        
    # 4번 선택 설정 
    elif select == 4 : 
        count = 0
        searching = input('검색 키워드: ')
        print('검색 결과: ')
        for k, v in dict_value.items() :
            if searching.lower() in k : 
                print(f'- {k} {v}권')
                count += 1
        if count == 0 :
            print('검색 결과가 없습니다.')
        print()
    
    # 잘못된 입력 설정 
    elif select > 5 or select < 1 :
        print('잘못된 입력입니다.\n')
    
    # 5번 종료 설정 
    else : 
        break
print('프로그램을 종료합니다.')