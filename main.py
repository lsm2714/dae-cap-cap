# 쇼핑몰 주문 총액 계산기 

# 상품을 입력하는 함수 (반복) 
def main() :
    name = input('상품명 입력 (quit 입력 시 종료): ')
    if name == 'quit' : 
        return name 
    else : 
        # 이미 cart에 저장되어 있는 상품일 경우 가격 패스 (다른 가격 입력 방지)
        if name not in cart : 
            price = int(input('가격: '))
            # 음수 가격 입력 방지 
            if price < 0 : 
                while True : 
                    print('잘못된 입력입니다. 올바른 가격을 입력해 주세요.')
                    price = int(input('가격: '))
                    if price >= 0 :
                        break
                    else :
                        continue
                    
        else : 
            price = cart[name]['가격']
        qty = int(input('수량: '))
        # 음수 수량 입력 방지
        if qty < 1 :
            while True : 
                print('잘못된 수량입니다. 올바른 수량을 입력해 주세요.')
                qty = int(input('수량: '))
                if qty >= 1 :
                    break
                else :
                    continue
        return add_item(name, price, qty)

# 상품 개수와 가격을 받아 저장하는 함수
cart = {} 
def add_item(name, price, qty) : 
    if name not in cart : 
        cart[name] = {'가격' : price, '수량' : qty}
    else : 
        cart[name]['수량'] += qty

# 장바구니 내용을 출력하는 함수 
def print_cart(cart) : 
    print('\n장바구니: ')
    for k, v in cart.items() :
        print(f'- {k}: {v['가격']}원 x {v['수량']}개 = {v['가격'] * v['수량']}원')

# 상품들의 총액을 계산해 반환하는 함수
def calculate_total(cart) : 
    amount = 0 
    for v in cart.values() :
        amount += v['가격'] * v['수량']
    print(f'\n총액: {amount:,}원')
    
# main() 함수 반복 
result = ''
while result != 'quit' : 
    result = main() 

# print_cart 함수 호출 
print_cart(cart)

# calculate_total 함수 호출
calculate_total(cart) 
