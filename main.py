# 회문 검사하기 
# 문자열 입력하기 
input_value = input('Enter a string: ')

# 띄어쓰기, 특수문자 제거 
words = ''
for i in input_value :
    if i in ' ,.!?' :
        continue 
    words += i

# : 를 기준으로 리스트에 담기 + 대소문자 구분 없애기
list_value = words.split(':')
list_value = [i.lower() for i in list_value]

# 팰린드롬 검사 
if list_value[1] in list_value[0][::-1] :
    print('Palindrome')
else : 
    print('Not Palindrome')