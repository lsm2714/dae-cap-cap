# 학생 성적 출력, 최고점 학생(들) 출력 
# 종료 입력할 때까지 반복 설정 
dict_value = {} 
print('학생 이름과 성적을 입력하세요 (종료 입력시 종료): ')
while True : 
    student = input() 
    if student == '종료' : 
        break
    student = student.split() 
    if student[0] not in dict_value : 
        dict_value[student[0]] = [int(student[1])]
    else : 
        dict_value[student[0]].append(int(student[1]))

# 학생별 평균 점수 출력 
avgs = 0
print('\n--- 학생별 평균 점수 ---')
for k, v in dict_value.items() : 
    avg = sum(v) / len(v)
    print(f'{k}: {avg:.1f}')
    if avg >= avgs :
        avgs = avg

names = []
for k, v in dict_value.items() : 
    if (sum(v) / len(v)) == avgs : 
        names.append(k)
print(f'최고 평균 점수 학생: {names} ({avgs}점)')



    

        
        



