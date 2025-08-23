# 완전수 판별기
# 정수 입력받기 
number = int(input('정수를 입력하세요: '))

# 약수 구해서 리스트에 집어넣기 
list_value = [num1 for num1 in range(1, number + 1) if number % num1 == 0]

# 완전수 구하기 
if sum(list_value) - number == number : 
    print(f'{number}는 완전수입니다.')
else :
    print(f'{number}는 완전수가 아닙니다.')
    


    

        
        



