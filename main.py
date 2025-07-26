def check_password(PW) :
    if 8 <= len(PW) :
        pass
    else : 
        return '사용 불가: 조건을 만족하지 않습니다.'
    if any(c.isupper() for c in PW) :
        pass
    else : 
        return '사용 불가: 조건을 만족하지 않습니다.'
    if any(c.islower() for c in PW) :
        pass
    else : 
        return '사용 불가: 조건을 만족하지 않습니다.'
    if any(c.isdigit() for c in PW) :
        pass 
    else : 
        return '사용 불가: 조건을 만족하지 않습니다.'
    kals = []
    for c in PW :
        kals.append(c)
    if "!" or '@' or '#' or '$' or '%' or '^' or '&' or '*' in kals :
        return '사용 가능한 비밀번호입니다.'
    else : 
        return '사용 불가: 조건을 만족하지 않습니다.'

PW = input() 

result = check_password(PW)

print(result)
