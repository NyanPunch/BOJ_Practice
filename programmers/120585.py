# 머쓱이보다 키 큰 사람 120585
def solution(array, height):
    answer = 0
    array.sort(reverse = True)
    i = 0
    
    while (array[i] > height):
        answer += 1
        i += 1
        if(len(array) <= i): break
    
    return answer
