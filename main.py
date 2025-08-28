# 현금 인출 프로그램
# 딕셔너리에 돈 저장하기 
list_value = [50000, 10000, 5000, 1000, 500, 100, 50, 10] 
dict_value = {} 
keys = [str(i) + '원' for i in list_value]
for i in keys : 
    dict_value[i] = 0
# 인출 금액 입력받기 
money = int(input('인출할 금액을 입력하세요: '))
if money < 10 :
    print('10원 이하는 인출할 수 없습니다.')
    exit() 

# 계산 
print('지폐 계수: ')
for num in list_value :  
    while money >= num : 
        money -= num
        dict_value[f'{num}원'] += 1

# 출력 
for k, v in dict_value.items() :
    if v == 0 :
        continue 
    # 1000원 이하일 경우 단위 = '개' 
    if len(k) <= 4 :
        print(f'{k}: {v}개')
    # 아니면 '장'
    else : 
        print(f'{k}: {v}장')

