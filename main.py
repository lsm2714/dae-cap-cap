# 도서 대출 관리 프로그램 
dict_value = {}

# 반복 설정을 위한 대출 권 수 입력 
while True : 
    number = int(input('대출할 책의 개수 입력: '))
    if number < 1 :
        print('잘못된 입력입니다. 1 이상의 수를 입력해 주세요.')
    else : 
        break 
    
# 책 이름과 권수 반복 입력 
print('책 이름과 권수 입력 (띄어쓰기 기준): ')
for _ in range(number) : 
    book = input().split()
    # 딕셔너리에 저장 (중복 시 잘못된 입력 처리)
    if book[0] not in dict_value : 
        dict_value[book[0]] = int(book[1])
    # 잘못된 입력 반복 설정
    else : 
        while True : 
            print('잘못된 입력입니다. 다시 입력해 주세요.')
            book = input().split()
            if book[0] not in dict_value :
                break
            else : 
                continue
        
    
    
