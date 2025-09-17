# 단어 뒤집기 암호 
list_value = []

# 단어 입력 
sentence = input('Enter a sentence: ').split()

# 홀수는 그대로 놔두고 짝수 자리만 뒤집기 
count = 1
for i in sentence : 
    if count % 2 == 0 :
        i = i[::-1]
    count += 1
    list_value.append(i)

# 결과 출력 
print(f' '.join(list_value))
