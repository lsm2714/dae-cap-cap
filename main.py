# 택배 상자 쌓기 
# 박스 입력 
box_numbers = input('Enter boxes: ').split()
if box_numbers == [] :
    print('입력된 박스가 없습니다.')
    exit() # 종료
box_numbers = [int(i) for i in box_numbers] # 정수형 변환 

# 박스 더미 개수 새기 
# 뒤에 오는 숫자가 앞의 숫자보다 크거나 같을 경우 상자를 쌓을 수 있고 
# 뒤에 오는 숫자가 앞의 숫자보다 작을 경우 새로운 더미를 만든다.
count = 1
list_value = []
# 반복 설정 
for i in box_numbers : 
    if list_value != [] : # 비어있지 않을 경우
        # i가 더 작을 경우 더미 개수 추가 
        if i < list_value[-1] : 
            count += 1
    list_value.append(i)

# 결과 출력 
print(f'박스 더미 개수: {count}')
