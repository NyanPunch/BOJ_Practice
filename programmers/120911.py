# 문자열 정렬하기 (2) 120911
def solution(my_string):
    s1 = my_string.lower()
    s2 = sorted(s1)
    #print(s2)
    answer = ''.join(sorted(s2))
    return answer
