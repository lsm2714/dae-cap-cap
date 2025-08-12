# 학생들의 점수 리스트 
scores = [92, 85, 34, 76, 58, 90, 61, 70, 45, 99, 82, 67, 50, 77, 89]

# 등급별로 딕셔너리에 저장 
scores_dict = { 
    'A': [i for i in scores if i >= 90],
    'B': [i for i in scores if 90 > i >= 80],
    'C': [i for i in scores if 80 > i >= 70],
    'D': [i for i in scores if 70 > i >= 60],
    'F': [i for i in scores if 60 > i]
}

# 각 등급의 평균 점수와 그래프 출력 
print('등급 분포 및 평균 점수: ')
for k, v in scores_dict.items() : 
    print(f'{k}등급: 평균 점수 = {(sum(v) / len(v)):.2f}')
    for _ in v : 
        print('*', end='')
    print(f' ({len(v)}명)')
    
            
    


    

    



            
            
    




