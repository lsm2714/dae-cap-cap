# 가장 긴 단어 찾기 
# String 입력 
input_value = input()
words = ''

# 특수 문자 제거 후 리스트로 변경 
for i in input_value : 
    if i in '.,!?' :
        words += ' '
        continue
    words += i 
    
words = words.split() 
words_2 = []
for i in words :
    if i not in words_2 : 
        words_2.append(i)
    
# max_value 설정 
max_value = max(words)
max_value = len(max_value)

# 가장 긴 단어 찾기 설정
for i in words_2 :
    if len(i) == max_value :
        print(f'가장 긴 단어: {i} (길이: {max_value})')
