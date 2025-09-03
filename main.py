# 단어 빈도수 세기 
dict_value = {} 
# 반복 설정 
while True : 
    # 문장 입력
    words = input('문장 입력 (빈 줄 입력 시 종료): ')

    # 특수 문자 제거 후 띄어쓰기를 기준으로 리스트에 저장 
    new_words = ''
    for i in words : 
        if i in '.,!?' :
            continue 
        new_words += i 
    new_words = new_words.split() 
    
    # new_words == [] 일 경우 종료 
    if new_words == [] :
        break

    # 딕셔너리에 넣기 
    for ele in new_words : 
        # dict_value에 없을 경우에는 새로 추가 
        if ele not in dict_value : 
            dict_value[ele.lower()] = 1 
        # 있으면 1추가 
        else : 
            dict_value[ele.lower()] += 1 

# 딕셔너리 value값이 큰 순으로 정렬 후 결과 출력 
dict_value = sorted(dict_value.items(), key=lambda x: x[1], reverse=True)
print('\n단어 빈도수: ')
if dict_value != {} : 
    for e in dict_value :
        print(f'{e[0]}: {e[1]}')
else : 
    print('\n입력된 문장이 없습니다.')
