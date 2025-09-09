# 두 수의 합 
# 숫자들 공백으로 입력 
numbers = input('Enter numbers: ').split() 
numbers = [int(i) for i in numbers]
count = 0
indexs = []
for _ in numbers : 
    indexs.append(count)
    count += 1

# 타겟 입력 
target = int(input('Enter target: '))

# 반복 설정 
for i1 in indexs : 
    for i2 in indexs :
        if i1 == i2 :
            continue
        if numbers[i1] + numbers[i2] == target : 
            print(f'{i1}, {i2}')
            exit()

# 아무것도 출력 안되면 
print('두 수를 합해서 target이 나올 경우의 수가 없습니다.')
        

        
