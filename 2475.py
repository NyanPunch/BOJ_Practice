n = list(map(int, input().split()))
print(sum([i**2 for i in n]) % 10)
# 각 수를 제곱하여 더한 후 10으로 나눈 나머지 출력
