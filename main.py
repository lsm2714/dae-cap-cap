def check_pw(pw) : 
    if 8 <= len(pw) :
        pass
    else : 
        return '올바르지 않은 비밀번호입니다.'
    if any(c.isdigit() for c in pw) :
        pass 
    else : 
        return '올바르지 않은 비밀번호입니다.'
    if any(c.isupper() for c in pw) :
        pass 
    else : 
        return '올바르지 않은 비밀번호입니다.'
    if any(c.islower() for c in pw) :
        pass 
    else : 
        return '올바르지 않은 비밀번호입니다.'
    if any(c in '!@#$%^&*' for c in pw) :
        pass 
    else : 
        return '올바르지 않은 비밀번호입니다.'
    return '올바른 비밀번호입니다.'

pw = input() 

result = check_pw(pw)

print(result)