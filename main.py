menu_list = ['입고', '판매', '설정']
dict_value = {} 

# 반복 설정 
while True : 
    menu = input('\n작업을 입력하세요 (입고/판매/종료): ')
    if menu == '종료' :
        break
    if menu not in menu_list :
        print('올바른 입력이 아닙니다.') 
        continue
    name = input('상품명을 입력하세요: ')    
    number = int(input('수량을 입력하세요: '))
    # 만약 상품명이 dict_value에 없을 경우 새로 추가 
    if (name not in dict_value) and (menu == '입고'): 
        dict_value[name] = number
    # 만약 상품명이 dict_value에 있을 경우 작업에 따라 알맞은 계산 실행 
    else : 
        if menu == '입고' : 
            dict_value[name] += number
        elif menu == '판매' : 
            if name not in dict_value :
                print('등록되지 않은 상품입니다.')
            else : 
                dict_value[name] -= number 
                if dict_value[name] < 1 : 
                    print('재고 부족')
                    dict_value[name] += number

# 결과 출력 (재고)
if dict_value == {} :
    print('상품이 등록되어 있지 않습니다.')
else : 
    print('--- 현재 재고 ---')
    for k, v in dict_value.items() :
        print(f'{k}: {v}개')


            
            
    




