# 주민번호 입력 
while True : 
    number = input('주민번호를 입력하세요: ')
    if len(number) != 14 :
        print('올바른 주민번호 형식이 아닙니다.')
    else :
        break

print(f'마스킹된 주민번호: {number[:8]}',end='') 
print('******')
    
    




