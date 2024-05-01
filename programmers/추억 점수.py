# 그리움 점수 합산 값 = 추억 점수
def solution(name, yearning, photo):
    answer = []
    dic = dict(zip(name, yearning))
    
    for i in photo:
        temp = list(set(name) & set(i))
        point = sum(dic[name] for name in temp if name in dic)
        answer.append(point)
    
    return answer
