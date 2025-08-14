# 가장 긴 단어 찾기 
input_value = input() 
list_value = input_value.split() 

kaka = [] 
for i in list_value : 
    kaka.append(i)
    
for _ in kaka : 
    if len(kaka[0]) > len(kaka[1]) : 
        del kaka[1]
    else : 
        del kaka[0]
print(kaka[0])





