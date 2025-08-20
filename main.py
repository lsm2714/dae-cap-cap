# 아나그램 판별기 만들기 
# 문자열 입력 
input_value = input('첫 번째 문자 입력: ')
list_value = [i.lower() for i in input_value] 
input_value2 = input('두 번째 문자 입력: ')
list_value2 = [i.lower() for i in input_value2]

# 아나그램 확인 
for w in list_value2 : 
    for i, e in enumerate(list_value) : 
        if w == e : 
             del list_value[i]
if list_value == [] : 
    print('아나그램입니다.')
else : 
    print('아나그램이 아닙니다.')


        
        



