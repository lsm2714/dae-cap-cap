# 함수 복습 
def calculate(x, y) :
    if y == 0 : 
        q = '0으로 나눌 수 없습니다.'
    else : 
        q = f'{(x/y):.2f}'
    return x+y, x-y, x*y, q # 이렇게 하면 튜플의 형태로 반환됨 

# 숫자 2개 입력 
num1 = int(input('첫 번째 숫자 입력: '))
num2 = int(input('두 번째 숫자 입력: '))
a, b, c, d = calculate(num1, num2) # 튜플 자릿수에 맞춰서 변수에 각각 넣어주기
print(f'합: {a}\n차: {b}\n곱: {c}\n몫: {d}')