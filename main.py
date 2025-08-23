# 팩토리얼 자릿수 계산 
# 팩토리얼 입력받기 
list_value = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '!']
pacto = input('팩토리얼을 입력하세요: ')
if pacto == '!' :
    print('팩토리얼을 입력하세요.')
    exit() 
for i in pacto : 
    if i not in list_value or '!' not in pacto : 
        print('팩토리얼을 입력하세요.')
        exit() 

# '!' 제외 후 리스트에 넣기 
number = pacto.split('!')
del number[-1]

# 팩토리얼 계산하기 
num = 1
for n in range(1, int(number[0]) + 1) : 
    num *= n 
print(f'팩토리얼 계산 값: {num}')

# 자릿수 계산하기 
num = str(num)
num_list = [int(i) for i in num]

num2 = 0 
for n in num_list : 
    num2 += n 
print(f'팩토리얼 자릿수 계산 값: {num2}')



    

        
        



