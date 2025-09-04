# 랜덤 비밀번호 생성기 
import random 

uppers = 'QAZWSXEDCRFVTGBYHNUJMIKOLP'
lowers = uppers.lower() 
digits = '1234567890'
special = '!@#$%^&*'
all_value = uppers + lowers + digits + special

# 비밀번호 길이 입력 
while True : 
    length = int(input('비밀번호 길이 입력: '))
    if length < 6 :
        print('비밀번호 길이가 너무 짧습니다. 다시 입력해주세요.')
        continue
    elif length > 20 : 
        print('비밀번호 길이가 너무 깁니다. 다시 입력해주세요.')
        continue
    else : 
        break

# 올바른 비밀번호가 나올 때까지 반복 설정 
while True : 
    # 비밀번호 생성 
    password = '' 
    for i in random.sample(all_value, length):
        password += i 
    
    # 조건 설정 (대소문자 각각 최소 1개, 숫자 최소 1개, 특수문자 최소 1개) 
    has_upper = any(i.isupper() for i in password)
    has_lower = any(i.islower() for i in password)
    has_digit = any(i.isdigit() for i in password)
    has_special = any(i in special for i in password)

    # 전부 True일 경우 break
    if has_digit and has_lower and has_upper and has_special :
        break

print(f'생성된 비밀번호: {password}')