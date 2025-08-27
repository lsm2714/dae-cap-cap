# 숫자 빈도 출력기 
dict_value = {} 

# 반복 설정 
while True : 
    
    # 정수 입력
    number = int(input('정수 입력 (0 입력 시 종료): '))
    
    # 입력이 0이 아닐 경우 설정 
    if number != 0 :
        # dict_value에 없을 경우 새로 생성 후 value값을 1로 설정 
        if number not in dict_value : 
            dict_value[number] = 1
        # 있을 경우 value값에 1 추가 
        else : 
            dict_value[number] += 1 
    # 0일 경우 break로 반복문 빠져나가기
    else : 
        break

# 결과 출력 
print('결과: ')
if dict_value == {} : 
    print('저장된 숫자가 없습니다.')
else : 
    for k, v in (sorted(dict_value.items())) : 
        print(f'{k}: {v}회')

