# 학생 성적 관리 프로그램 
dict_value = {} 
scores = []

# 학생 정보 입력 설정 (반복)
print('학생 이름과 점수를 입력하세요 (종료 입력 시 멈춤): ')
while True : 
    student = input()
    if student == '종료' : 
        break
    student = student.split() 
    dict_value[student[0]] = int(student[1])

# 바로 종료 입력 시 
if dict_value == {} : 
    print('\n저장된 학생 정보가 없습니다.')
    exit()
    
# 메뉴 선택 설정 (반복)
while True : 
    select = int(input('''\n메뉴를 선택하세요: 
1. 전체 학생 목록 보기 
2. 평균 점수 구하기
3. 최고 점수 학생 찾기
4. 특정 학생 점수 조회
5. 종료
선택: '''))
    
    # scores 리스트에 점수 집어넣기 
    for v in dict_value.values() :
        scores.append(v)
        
    # 1번 선택 설정 
    if select == 1 : 
        for k, v in dict_value.items() :
            print(f'- {k}: {v}점')
            
    # 2번 선택 설정 
    elif select == 2 :
        print(f'평균 점수: {(sum(scores) / len(scores)):.1f}')
    
    # 3번 선택 설정 
    elif select == 3 :
        max_score = max(scores)
        for k in dict_value.keys() : 
            if dict_value[k] == max_score :
                print(f'최고 점수 학생: {k} ({max_score}점)')
    
    # 4번 선택 설정 
    elif select == 4 :
        search = input('조회할 학생 이름: ')
        if search not in dict_value : 
            print('저장되어 있지 않은 학생입니다.')
        else : 
            print(f'{search}의 점수: {dict_value[search]}점')
        
    # 5번 선택 설정 
    elif select == 5 : 
        break
    
    # 잘못된 입력 설정 
    else : 
        print('잘못된 입력입니다. 1부터 5 사이의 숫자 중 선택하세요.')
        
print('프로그램을 종료합니다.')
            
    