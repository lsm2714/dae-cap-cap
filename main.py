# 학생들의 점수 리스트 
scores = [92, 85, 34, 76, 58, 90, 61, 70, 45, 99]

# 등급별로 딕셔너리에 저장 
scores_dict = { 
    '우수': [i for i in scores if i >= 90],
    '양호': [i for i in scores if 90 > i >= 70],
    '보통': [i for i in scores if 70 > i >= 50],
    '미흡': [i for i in scores if 50 > i]
}
    
# 각 등급에 들어있는 점수와 평균 출력 
for k, v in scores_dict.items() : 
    print(f'{k}: {v} 평균: {(sum(v) / len(v)):.2f}')
    
            
    


    

    



            
            
    




