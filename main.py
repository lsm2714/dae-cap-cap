# 숫자 통계 프로그램 
numbers_list = []

# 반복 설정 + 0 입력 시 break 
while True : 
    num = int(input('숫자 입력 (0 입력 시 종료): '))
    if num == 0 :
        break
    numbers_list.append(num)

# 결과 출력 
if numbers_list : # 빈 리스트는 False로 구분되기 때문에 그냥 놔두면 됨 
    # 딕셔너리에서 계산
    dict_value = {
    '합' : sum(numbers_list),
    '평균' : sum(numbers_list) / len(numbers_list),
    '최댓값' : max(numbers_list),
    '최솟값' : min(numbers_list),
    '짝수 개수' : len([i for i in numbers_list if i % 2 == 0]),
    '홀수 개수' : len([i for i in numbers_list if i % 2 != 0])
    }
    print('\n결과: ')
    for k, v in dict_value.items() : 
        print(f'{k}: {v}')
else : 
    print('\n저장된 숫자가 없습니다.')
