checklist = [0] * 4
mylist = [0] * 4
count = 0

def myadd(c):
    global checklist, mylist, count
    if c == 'A':
        mylist[0] += 1
        if mylist[0] == checklist[0]:
            count += 1
    elif c == 'C':
        mylist[1] += 1
        if mylist[1] == checklist[1]:
            count += 1
    elif c == 'G':
        mylist[2] += 1
        if mylist[2] == checklist[2]:
            count += 1
    elif c == 'T':
        mylist[3] += 1
        if mylist[3] == checklist[3]:
            count += 1
            
def myremove(c):
    global checklist, mylist, count
    if c == 'A':
        if mylist[0] == checklist[0]:
            checklist -= 1
        mylist[0] -= 1
    elif c == 'C':
        if mylist[1] == checklist[1]:
            checklist -= 1
        mylist[1] -= 1
    elif c == 'G':
        if mylist[2] == checklist[2]:
            checklist -= 1
        mylist[2] -= 1
    elif c == 'T':
        if mylist[3] == checklist[3]:
            checklist -= 1
        mylist[3] -= 1
        
S, P = map(int, input().split())
result = 0
A = list(input())
checklist = list(map(int, input().split()))

for i in range(4):
    if checklist[i] == 0:
        count += 1
        
for i in range(P):
    myadd(A[i])
    
if count == 4:
    result += 1

for i in range(P, S):
    j = i - P
    myadd(A[i])
    myremove(A[j])
    if count == 4:
        result += 1
        
print(result)
