num1 = float(input('기본값을 입력하세요 : '))

print('''1. 더하기
2. 빼기
3. 곱하기
4. 나누기''')

def select(num1) : 
    sel = int(input('선택: '))
    if sel == 1 :
        num2 = int(input('숫자 입력: '))
        return f'연산 결과: {num1 + num2}'
    elif sel == 2 :
        num2 = int(input('숫자 입력: '))
        return f'연산 결과: {num1 - num2}'
    elif sel == 3 :
        num2 = int(input('숫자 입력: '))
        return f'연산 결과: {num1 * num2}'
    elif sel == 4 :
        num2 = int(input('숫자 입력: '))
        if num2 == 0 :
            return '에러 : 0으로 나눌 수 없습니다.'
        else : 
            return f'연산 결과: {num1 / num2}'
    else : 
        return '에러 : 범위 밖의 숫자를 선택하셨습니다.'

result = select(num1) 

print(result)




    
