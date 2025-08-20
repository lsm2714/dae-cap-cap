# 소수 판별기 
# 숫자 입력 후 리스트에 담기 
number = int(input('숫자를 입력하세요: ')) 
numbers = [num for num in range(2, number + 1)]

# for 반복문으로 소수 판별하기 
list_value = []
for num1 in numbers : 
    check_list = []
    for num2 in range(2, num1) : 
        num = num1 % num2
        if num == 0 : 
            check_list.append(num)
    if check_list == [] :
        list_value.append(num1)

print(list_value)


        
        



