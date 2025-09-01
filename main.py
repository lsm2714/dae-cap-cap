# 오늘 날짜와 목표 날짜 
from datetime import date 

# 목표 날짜 입력받고 저장하기 + 오늘 날짜도 저장 
year = int(input('연도 입력: '))
month = int(input('월 입력: '))
day = int(input('일 입력: '))

Target_day = date(year, month, day) # 목표 날짜 
today = date.today() # 오늘 날짜 

# 오늘 날짜와 목표 날짜 출력 
print(f'\n오늘 날짜: {today}')
print(f'목표 날짜: {Target_day}')

# 날짜 차이 계산하고 알맞은 출력 설정 
diff = (Target_day - today).days # days하면 날짜 숫자만 저장됨 
if diff > 0 :
    print(f'D-day: {diff}일 남았습니다.')
elif diff < 0 :
    print(f'{abs(diff)}일 지났습니다.') # abs() 함수 사용으로 정상화 
else : 
    print('오늘입니다!')
