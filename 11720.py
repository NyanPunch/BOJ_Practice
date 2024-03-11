# 숫자의 합
n = int(input())
numbers = list(map(int, list(input().strip())))
sum = 0

for i in numbers:
    sum += i
    
print(sum)
    
