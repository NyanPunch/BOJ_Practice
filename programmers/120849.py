# 모음 제거
def solution(my_string):
    answer = ''
    a = ['a', 'i', 'u', 'e', 'o']
    
    for i in my_string:
        if i in a:
            my_string = my_string.replace(i, '')
    
    answer = my_string         
    return answer
