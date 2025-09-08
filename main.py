# 완전수 판별하기 
# 정수 입력받기 
number = int(input('Enter a number: '))

# 약수 구하기 (n%d 했을 때 나머지가 0이 되는 수)
numbers_list = []
for i in range(1, number) :
    if number % i == 0 :
        numbers_list.append(i)

# 자신을 제외한 약수를 모두 더했을 때의 수가 number과 같을 경우 완전수 
perfect_number = 0
for i in numbers_list :
    perfect_number += i

# 결과 출력
if perfect_number == number :
    print(f'{number} is a Perfect Number')
else : 
    print(f'{number} is not a Perfect Number')