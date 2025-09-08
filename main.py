# 단어 등장 횟수 세기 
dict_value = {} 

# 입력 설정 
input_value = input('Enter a sentence: ')

# 특수 문자와 띄어쓰기 제거 후 리스트에 집어넣기 + 사전순 정렬
words = ''
for i in input_value : 
    if i in '.,!?' :
        continue
    words += i
list_value = sorted(words.split())

# 소문자 전환 
list_value = [i.lower() for i in list_value]

# 단어 출력 횟수 세기 
for i in list_value :
    # dict_value에 없을 경우 1과 함께 추가 
    if i not in dict_value : 
        dict_value[i] = 1
    # 있을 경우 +1 
    else : 
        dict_value[i] += 1

# 결과 출력 
for k, v in dict_value.items() :
    print(f'{k} : {v}')