# 문장 입력 받기 
input_value = input('문장을 입력하세요: ') 
words = input_value.split() 

# 4글자 이상인 문자만 리스트에 담기 
list_value = []
for w in words : 
    if len(w) >= 4 :
        list_value.append(w.upper())

# 공백으로 나눠서 출력하기 
print(' '.join(list_value))


            
        
        
    






