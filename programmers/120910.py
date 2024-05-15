# 세균 증식 120910
def solution(n, t):
    answer = n
    i = 0
    while i < t:
        answer *= 2
        i += 1
    return answer
