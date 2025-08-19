# 문자열 입력받기 
input_value = input('문장을 입력하세요: ')
words = input_value.split()

# 문자열 길이에 따라 딕셔너리에 저장하기 
dict_value = {} 
for w in words : 
    if len(w) not in dict_value : 
        dict_value[len(w)] = [w]
    else : 
        dict_value[len(w)].append(w)

# 결과 출력하기 
if dict_value == {} :
    print('입력한 문자가 없습니다.')
else : 
    print('--- 입력한 문자들의 길이 ---')
    for k, v in dict_value.items() :
        print(f'{k}: {', '.join(v)}')



