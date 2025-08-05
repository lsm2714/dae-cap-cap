# 공백을 기준으로 문자열에서 특정 단어의 출현 횟수 검출하기 
input_value = input('문자열 입력: ')
input_value = input_value.split()

word = input('단어 입력: ')

count = 0 
for i in input_value :
    if i == word :
        count += 1
print(f'단어 "{word}"의 출현 빈도: {count}')
    


            
            
    




