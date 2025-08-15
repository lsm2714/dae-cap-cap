# 문자 입력 받기 
input_value = input('문자열을 입력하세요: ') 
words = input_value.split() 

bad_word = input('금지 문자를 입력하세요: ')

# 금지어 포함된 문자 구분 
list_value = [] 
for w in words : 
    if bad_word in w : 
        continue
    list_value.append(w)

# 결과 출력 
print(' '.join(list_value))
            
        
        
    






