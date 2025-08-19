# 문자열 입력받기 
input_value = input('문장을 입력하세요: ')
words = input_value.split()
words = [i.lower() for i in words]

# 단어가 나온 횟수를 딕셔너리에 저장 
dict_value = {} 
for w in words : 
    if w not in dict_value : 
        dict_value[w] = 1 
    else : 
        dict_value[w] += 1

# 딕셔너리 출력, 최빈값 출력 
if dict_value == {} :
    print('입력된 단어가 없습니다.')
else : 
    values = []
    max_keys = []
    print('--- 단어 빈도 ---')
    for k, v in dict_value.items() :
        print(f'{k}: {v}회')
    max_value = max([v for v in dict_value.values()])
    max_keys = [k for k in dict_value.keys() if dict_value[k] == max_value]
    print(f'가장 많이 나온 단어: {max_keys} ({max_value}회)')



