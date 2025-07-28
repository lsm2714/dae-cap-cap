# 주민 번호 입력
number = input('주민번호를 입력하세요 : ')

# '-'를 제외하고 모든 숫자 정수형으로 바꿔서 집어넣기 
num_list = []
for i in number :
    if i == '-' :
        continue
    num_list.append(i)
num_list = [int(i) for i in num_list]

Xnum = [2, 3, 4, 5, 6, 7, 8, 9, 2, 3, 4, 5]

# 앞 12자리 숫자를 위 리스트의 숫자와 각각 곱하기 + 값 모두 더하기 
num_list_add = []
count = 0
for num1 in Xnum :
    num2 = num_list[count] 
    num3 = num2 * num1
    num_list_add.append(num3)
    count += 1 
sum_value = sum(num_list_add)

# 계산할 거 계산 
last_num = (11 - (sum_value % 11)) % 10 
if last_num >= 10 :
    last_num -= 10 
print(last_num)
    
# 결과 확인 
if last_num == num_list[-1] :
    print('유효한 주민번호입니다.')
else : 
    print('유효하지 않은 주민번호입니다.')


    
