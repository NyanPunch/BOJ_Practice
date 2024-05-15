# 문자열안에 문자열 120908
def solution(str1, str2):
    answer = 2

    for i in range(len(str1)):
        if str1[i:i+len(str2)] == str2:
                return 1
    
    return answer
