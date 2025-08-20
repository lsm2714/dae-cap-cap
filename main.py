# 중복 제거 후 정렬
# 숫자 입력 후 리스트에 담기 
numbers = input('숫자들을 입력하세요: ')
numbers = [int(i) for i in numbers if i != ' ']

# 중복 제거 후 리스트에 오름차 순으로 담기 
list_value = [] 
for num in numbers : 
    if num not in list_value : 
        list_value.append(num)

num_list = [] 
while list_value != [] : 
    min_value = min(list_value)
    num_list.append(min_value)
    for i, v in enumerate(list_value) :
        if v == min_value : 
            del list_value[i]
    
print(num_list)
    
    
    



    

        
        



