while True:
    mylist = list(map(int, input().split()))
    if mylist[0] == 0 and mylist[1] == 0 and mylist[2] == 0:
        break
    mylist.sort()

    if mylist[0]**2 + mylist[1]**2 == mylist[2]**2:
        print('right')
    else:
        print('wrong')
