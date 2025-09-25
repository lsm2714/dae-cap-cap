# 소수 판별기 (함수 사용)

# 숫자 입력받고 출력하는 함수 설정 
def main() : 
    number = int(input('숫자를 입력하세요: '))
    if number <= 1 :
        return '소수가 아닙니다.'
    if is_prime(number) : 
        return f'{number}은(는) 소수입니다.'
    else : 
        return f'{number}은(는) 소수가 아닙니다.'

# 소수 판별하는 함수 설정 
def is_prime(n) :
    list_value = []
    for num in range(2, n) :
        result = n % num 
        list_value.append(result)
    if 0 not in list_value : 
        return True
    else : 
        return False 

# main 함수 호출 + 결과 출력 
print(main())

