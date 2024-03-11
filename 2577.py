a = input()
b = input()
c = input()

result = int(a) * int(b) * int(c)
result = str(result)

for i in range(10):
    print(result.count(str(i)))
