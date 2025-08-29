# 로또 당첨 시뮬레이터 
# 랜덤으로 6개 번호 생성
import random 
numbers = [i for i in range(1, 46)]
ran_list = [i for i in random.sample(numbers, 6)]
ran_list = sorted(ran_list)
ranking_list = ['꽝', '꽝', '꽝', '4등', '3등', '2등', '1등']

# 공백을 기준으로 번호 6개 입력 
your_numbers = input('번호 6개를 입력하세요 (1~45, 공백 구분): ').split()
your_numbers = [int(i) for i in your_numbers]

# 일치 수 확인, 등수 결정 
count = 0 
for num in your_numbers : 
    if num in ran_list :
        count += 1

for i in range(7) :
    if count == i :
        result = ranking_list[i]

# 결과 출력 
print(f'당첨 번호: {", ".join([str(i) for i in ran_list])}')
print(f'내 번호: {", ".join([str(i) for i in your_numbers])}\n')
print(f'맞춘 개수: {count}개')
print(f'결과: {result}')

