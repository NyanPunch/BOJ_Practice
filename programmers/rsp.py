def solution(rsp):
    answer = ''
    for i in rsp: # 2 : scissor, 0 : rock, 5 : paper
        if i == "2": answer += "0"
        if i == "5": answer += "2"
        if i == "0": answer += "5"
    return answer
