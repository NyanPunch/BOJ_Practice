# 잘라서 배열로 저장하기 120913
def solution(my_str, n):
    answer = []
    i = 0
    temp = ''
    while i < len(my_str):
        if i % (n) == 0 and i != 0:
            answer.append(temp)
            temp = ''
        temp += my_str[i]
        i += 1
    if temp != '': answer.append(temp)
    return answer
