value1 = int(input('첫 번째 수 : '))
value2 = int(input('두 번째 수 : '))
value3 = int(input('세 번째 수 : '))

if value1 == value2 == value3 :
    print('모든 수가 같습니다.')
    
if (value1 == value2 and value1 != value3) :
    print(f'두 수가 같습니다. {value1}와 {value2}')
if (value1 == value3 and value2 != value3) :
    print(f'두 수가 같습니다. {value1}와 {value3}')
if (value3 == value2 and value1 != value2) :
    print(f'두 수가 같습니다. {value3}와 {value2}')
    
if value1 != value2 and value1 != value3 and value2 != value3 : 
    list_value = [value2, value1, value3]
    print(f'모든 수가 다릅니다. 가장 큰 수는 {max(list_value)}입니다.')