# 학점 계산기 

# 점수 입력하는 함수
def main() : 
    scores = []
    subjects = ['국어', '영어', '수학', '과학']
    # 점수 4회 반복 입력 (국, 영, 수, 과)
    for s in subjects : 
        input_score = int(input(f'{s} 점수 입력: '))
        # 점수를 리스트에 넣기 (음수일 경우 다시 입력)
        if input_score >= 0 : 
            scores.append(input_score)
        else : 
            while True : 
                input_score = int(input('잘못된 입력입니다. 다시 입력해 주세요.\n'))
                if input_score >= 0 :
                    scores.append(input_score)
                    break
                else : 
                    continue
    return scores

# 점수 받고 평균 반환하는 함수
def get_average(scores) : 
    avg = sum(scores) / len(scores) 
    return avg 

# 평균으로 학점 정하는 함수
def get_grade(avg) : 
    scores = [90, 80, 70, 60]
    credits = ['A', 'B', 'C', 'D']
    credit = ''
    for i, e in enumerate(scores) : 
        if avg >= e : 
            credit = credits[i]
            return credit
    if credit == '' : 
        return 'F'
        
# 점수 리스트 받을 변수
scores = main() 

# 평균 점수 받을 변수
avg = get_average(scores)

# 학점 받을 변수 
credit = get_grade(avg) 

# 결과 출력 
print(f'평균 점수: {avg:.1f}')
print(f'학점: {credit}')