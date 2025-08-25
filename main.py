# 팰린드롬 문장 검사기 
# 문장 입력 받기 
input_value = input('입력: ')
list_value = [i.lower() for i in input_value if i != ' ']

if list_value == list_value[::-1] : 
    print('팰린드롬입니다.')
else : 
    print('팰린드롬이 아닙니다.')
        



