# 제곱수 판별하기 120909
def solution(n):
    answer = 2
    root = int(n**(0.5))
    
    if root**2 == n:
        answer = 1
    
    return answer
