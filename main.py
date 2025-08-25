# 숫자 분해합 
# 정수 n 입력받기 
number = input('정수를 입력하세요: ')
while int(number) >= 10 : 
    number = sum([int(i) for i in str(number)])
print(f'최종 결과: {number}')


