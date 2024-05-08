# 숨어있는 숫자의 덧셈(1)
def solution(my_string):
    answer = 0
    nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    for i in my_string:
        if i in nums:
            answer += int(i)
    return answer
