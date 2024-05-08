# 정수 제곱근 판별
def solution(n):
    answer = 0
    root = int(n**(0.5))
    if root**2 == n:
        answer = (root+1)**2
    else:
        return -1
    return answer
