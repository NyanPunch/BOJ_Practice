# 중복된 숫자 개수 120583
def solution(array, n):
    answer = 0
    for i in array:
        if(i == n): answer += 1
    return answer
