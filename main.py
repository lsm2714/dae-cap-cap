# 문자열 입력, 리스트에 저장 
input_value = input()
list_value = input_value.split() 

# 딕셔너리에 각 단어의 길이와 함께 저장 
dict_value = {} 
for element in list_value : 
    if element not in dict_value : 
        dict_value[element] = len(element)

# 딕셔너리 출력 
print(dict_value)

# value가 5 이상인 key값만 출력 
keys = [k for k, v in dict_value.items() if v >= 5]
if keys != [] : 
    print('value가 5 이상인 key값들: ', ', '.join(keys))
else : 
    print('value가 5 이상인 key값들: 없음')
    
    






