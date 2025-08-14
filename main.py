# 리스트 설정  
list_value = []

# 학생의 이름, 나이, 점수 입력 
while True : 
    student = input()
    if student == 'END' or student == 'end' :
        break
    lv = student.split() 
    lv[1] = int(lv[1])
    lv[2] = int(lv[2])
    list_value.append(lv)  

# 20세 이상, 80점 이상의 2가지 조건을 모두 충족하는 학생 출력 
if list_value == [] : 
    print('저장된 학생 정보가 없습니다.')
else : 
    print('--- 20대 이상 80점 이상인 학생 정보 ---')
    for lis in list_value : 
        if lis[1] >= 20 and lis[2] >= 80 :
            for i in lis : 
                print(i, end=' ')
            print() 
            
        
        
    






