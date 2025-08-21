# 문자열 압축 
# 문자열 입력받기 
input_value = input('문자열을 입력하세요: ') 
words = []
list_value = []
for i in input_value : 
    if words and i != words[-1] : 
        list_value.append(words)
        words = []
    words.append(i)
list_value.append(words)

# 문자열 압축하기 
count = 0
str_value = ''
for i1 in list_value : 
    if len(i1) == 1 :
        str_value += i1[0]
    else : 
        count = 0
        for i2 in i1 : 
            count += 1 
        str_value += i1[0] + str(count)

if len(input_value) <= len(str_value) : 
    print(f'압축된 문자: {input_value}')
else : 
    print(f'압축된 문자: {str_value}')

    



    

        
        



