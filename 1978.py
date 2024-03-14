N = int(input())
A = list(map(int, input().split()))
count = 0

for i in range(N):
    if A[i] == 1:
        continue
    elif A[i] == 2:
        count += 1
    else:
        for j in range(2, A[i]):
            if A[i] % j == 0:
                break
        else:
            count += 1

print(count)
