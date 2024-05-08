# 문자열 정렬하기(1)
def solution(my_string):
    answer = []
    nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    for i in my_string:
        if i in nums:
            answer.append(int(i))
    answer.sort()
    return answer
