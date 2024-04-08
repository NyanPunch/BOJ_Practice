n = int(input())
for i in range(n):
    score = 0
    sum = 0
    for j in input():
        if j == 'O':
            score += 1
            sum += score
        else:
            score = 0
    print(sum)
