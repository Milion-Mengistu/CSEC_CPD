def policerecruits():
    n = int(input())
    events = list(map(int, input().split()))
    police = 0
    crimes = 0
    for event in events:
        if event == -1:
            if police == 0:
                crimes += 1
            else:
                police -= 1
        else:
            police += event
    print(crimes)
policerecruits()