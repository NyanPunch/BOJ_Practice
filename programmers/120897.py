# 약수 구하기 120897
# n = 1일때와 n = 어떤수의 제곱일때 확인할 것
def solution(n):
    answer = []
    i = 1
    while i <= n:
        if i in answer: break
        if n % i == 0:
            answer.append(i)
            if i == (n // i): break
            answer.append(n // i)
        i += 1
        
    return sorted(answer)
