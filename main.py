# 회문 판별기 (함수 사용)
def is_Palindrome(w) :
    if w == w[::-1] : 
        result = '회문입니다.'
    else : 
        result = '회문이 아닙니다.'
    return result

# 단어 입력하기 
word = input('문자 입력: ').replace(" ", "") # replace = 전 -> 후
print(is_Palindrome(word.lower()))