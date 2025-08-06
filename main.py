# 명시적 형변환 
numbers = input('숫자들을 쉼표로 구분하여 입력하세요: ')
numbers = numbers.split(', ')
numbers = [int(i) for i in numbers]

# 총합 계산 
num_list = []
for num in numbers : 
    num_list.append(num)
    if sum(num_list) > 100 :
        print('총합이 100을 초과하였습니다.')
        print(f'현재까지의 입력값들: {num_list}')
        print(f'최종 총합: {sum(num_list)}')
        exit()

print('총합이 100을 초과하지 않았습니다.')
print(f'입력된 모든 숫자들: {num_list}')
print(f'최종 총합: {sum(num_list)}')

        




            
            
    




