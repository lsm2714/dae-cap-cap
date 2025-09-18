# 단어 빈도수 세기 (함수 활용) 
def word_count(sentence) : 
    # 특수문자 ,.?!를 제외하기 
    test = ''
    for i in sentence : 
        if i in '.,!?' : 
            continue
        test += i
    # 띄어쓰기를 기준으로 리스트에 넣기 
    list_value = test.split()
    # 딕셔너리에 단어 : 빈도수 의 형태로 집어넣기 
    dict_value = {} 
    for i in list_value : 
        if i not in dict_value : 
            dict_value[i] = 1
        else : 
            dict_value[i] += 1
    # 딕셔너리 반환하기 
    return dict_value

# 문장 입력하기 + 소문자 처리 
words = input('문장 입력: ')
# 결과 출력하기 
print('단어 빈도수: ')
for k, v in word_count(words.lower()).items() : 
    print(f'{k}: {v}')