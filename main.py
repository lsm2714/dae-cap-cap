import random

def password(length) : 
    upper = 'QAZWSXEDCRFVTGBYHNUJMIKOLP' 
    lower = upper.lower() 
    digit = '1234567890'
    all = upper + lower + digit 
    
    while True : 
        pw_ran = ''
        for _ in range(length) :
            pw_ran = pw_ran + random.choice(all)
        
        if any(i.isdigit() for i in pw_ran) and any(i.islower() for i in pw_ran) and any(i.isupper() for i in pw_ran) :
            return pw_ran

pw = int(input('비밀번호의 길이를 입력하세요: '))

if pw <= 3 :
    print('비밀번호는 4자리 이상이여야 합니다.')
    exit() 

result = password(pw)

print(result)


    
