books = []

# 반복 설정 
while True :
    book = input('도서 제목을 입력하세요 (종료하려면 "종료" 입력): ')
    if book == '종료' :
        break
    books.append(book)

print(f'도서 목록: {books}')
    


    
