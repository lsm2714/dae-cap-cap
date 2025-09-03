# 비밀번호 유효성 검사기 
# 비밀번호 입력 
password = input('비밀번호 입력: ')

# 조건 만족하는지 확인
result = '비밀번호가 조건을 만족하지 않습니다.' 
# 1. 길이가 8자 이상 
if len(password) < 8 :
    print(result)
else : 
    # 2, 3. 대소문자 각각 최소 1개 포함 
    if not (any(i.isupper() for i in password) and any(i.islower() for i in password)) : 
        print(result)
    else : 
        # 4. 숫자 최소 1개 포함 
        if not any(i.isdigit() for i in password) :
            print(result)
        else : 
            # 5. 특수문자 최소 1개 포함
            if not any(i in '!@#$%^&*' for i in password) : 
                print(result)
            else : 
                print('안전한 비밀번호입니다.')
