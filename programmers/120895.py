# 인덱스 바꾸기 120895
def solution(my_string, num1, num2):
    answer = list(my_string)
    n1 = my_string[num1]
    n2 = my_string[num2]
    answer[num1] = n2
    answer[num2] = n1
    
    return ''.join(answer)
