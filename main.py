# 소수 구하기 
numbers = []

# 숫자 입력 
number = int(input('Enter a number: '))

# 소수 구하기 
for i1 in range(2, number + 1) : 
    list_value = []
    for i2 in range(2, i1) :
        value = i1 % i2
        list_value.append(value) 
    if 0 not in list_value :
        numbers.append(i1)

# 결과 출력 
print(numbers)
        
