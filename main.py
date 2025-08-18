# 문자열 입력 
input_value = input()

# 띄어쓰기를 기준으로 리스트에 담기 
list_value = input_value.split() 

# 글자 수가 짝수인 단어만 출력하기 
for i in list_value : 
    if len(i) % 2 == 0 :
        print(i)
        
    






