# 중복된 문자 제거
def solution(my_string):
    answer = ''
    word = str(set(my_string))
    for i in my_string:
        if i in word:
            answer += i
            word = word.replace(i, '')

    return answer
