# 로또 번호 생성기 
import random 
ranking = ['꽝', '꽝', '꽝', '5등', '4등', '3등', '1등']

# 무작위 로또 번호 생성 
ran_numbers = random.sample(range(1, 46), 7)
print(ran_numbers)

# 번호 입력 (공백으로 구분)
choice_numbers = input('번호 6개 입력 (공백으로 구분): ').split()
choice_numbers = [int(i) for i in choice_numbers]

# 당첨 번호와 보서스 번호 출력 
print(f'{sorted(ran_numbers[:6])} 보너스: {ran_numbers[-1]}')

# 일치 개수 확인 
correct = 0
special = False 
for i in choice_numbers  : 
    # 보너스 제외 6개 번호
    if i in ran_numbers[:6] : 
        correct += 1 
    # 보너스 번호
    if i == ran_numbers[-1] : 
        special = True 

# 일치 개수 출력 
matching = f'일치 개수: {correct}개'
if correct == 5 and special :
    print(matching + ' + 보너스')
else : 
    print(matching)

# 결과(등) 출력 
for i, e in enumerate(ranking) : 
    result = f'결과: {e}'
    if correct == i :
        if correct == 5 : 
            if special : 
                print(f'결과: 2등')
            else : 
                print(result)
            break
        else : 
            print(result)