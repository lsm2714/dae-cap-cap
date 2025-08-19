# 문자열을 숫자와 함께 입력받기 
input_value = input()

add = 0 
numbers = [str(i) for i in range(10)]
for num in input_value : 
    if num in numbers : 
        add += int(num)

print(f'총 합계: {add}')


    






