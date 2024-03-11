#수들의 합 5

N = int(input())

count = 1
sum = 1
s, e = 1, 1

while e != N:
    if sum == N:
        count += 1
        e += 1
        sum += e
    elif sum > N:
        sum -= s
        s += 1
    else:
        e += 1
        sum += e

print(count)
