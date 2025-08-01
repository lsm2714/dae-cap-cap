movie_dict = {} 

# 반복 설정 
while True : 
    name = input('영화 제목을 입력하세요: ')
    if name == '종료' :
        break
    number = float(input('평점을 입력하세요: '))
    # 만약 영화 제목이 movie_dict에 없을 경우 새 리스트 생성 
    if name not in movie_dict :
        movie_dict[name] = [number]
    # 만약 있을 경우 그 키 값에 평점을 append()로 추가 
    else : 
        movie_dict[name].append(number)
    
# 평점 결과 출력 
for k, v in movie_dict.items() :
    print(f'{k}: {v} -> 평균: {(sum(v) / len(v)):.2f}')






