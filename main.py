# 엘베 시뮬레이션 
# 띄어쓰기 기준으로 정수들 입력 
numbers = input('Enter floors: ').split()
numbers = [int(i) for i in numbers]

# 엘베 이동 시간 계산 
time = abs(1 - numbers[0])
count = 1
for i in numbers :
    if count < len(numbers) :
        time += abs(i - numbers[count])
    count += 1

print(f'총 이동 시간: {time}초')

        
