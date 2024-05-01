# 경우의 수
def solution(balls, share):
    answer = 1
    for n, m in zip(range(balls-share+1, balls+1), range(1, share+1)):
        answer = answer*n/m
    return answer
