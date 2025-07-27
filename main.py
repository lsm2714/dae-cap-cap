number = int(input('현재 온도(섭씨)를 입력하세요 : '))

if number >= 30 :
    result = '수영'
elif number >= 20 :
    result = '등산'
elif number >= 10 :
    result = '자전거 타기'
else : 
    result = '스키'

print(f'\n현재 온도 : {float(number)}도')
print(f'추천 활동 : {result}')
    
