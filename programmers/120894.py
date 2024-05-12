# 영어가 싫어요
def solution(numbers):
    answer = ''
    dic = {'zero': '0',
           'one': '1',
           'two': '2',
           'three':'3',
           'four': '4',
           'five':'5',
           'six': '6',
           'seven': '7',
           'eight':'8',
           'nine':'9'}
    temp = ''
    for n in numbers: # 한 알파벳씩 받아오기 O(n)
        temp += n 
        if temp in dic: # 만들어진 단어가 있을 시
            answer += dic[temp] # 해당되는 값 삽입 
            temp = '' # 초기화 및 반복
        
    return int(answer)
