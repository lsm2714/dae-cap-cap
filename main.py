# 문자열 입력받기 
input_value = input()

words = ''
for w in input_value.lower() : 
    if w == ' ' :
        continue
    words += w

# 문자열 등장 횟수 딕셔너리에 저장 
dict_value = {} 
for w in words : 
    if w not in dict_value : 
        dict_value[w] = 1 
    else : 
        dict_value[w] += 1 

print(dict_value)

    






