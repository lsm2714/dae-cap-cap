# 피보나치 수열 
# 정수형 입력받기 
number = int(input('입력: '))

pibonachi = [0, 1]

if number < 2 : 
    if number == 0 : 
        print(pibonachi[0:1])
    else :
        print(pibonachi)
else : 
    for _ in range(number + 1) :
        num = pibonachi[-2] + pibonachi[-1]
        pibonachi.append(num)
    print(pibonachi[:-2])

        
        



