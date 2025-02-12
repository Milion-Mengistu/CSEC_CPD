def serajanddima():
    n = int(input())
    ls = list(map(int, input().split()))
    seraj = 0
    dima = 0
    i = 0
    j = n-1
    while i <= j:
        if ls[i] > ls[j]:
            seraj += ls[i]
            i += 1
        else:
            seraj += ls[j]
            j -= 1
        if i <= j:
            if ls[i] > ls[j]:
                dima += ls[i]
                i += 1
            else:
                dima += ls[j]
                j -= 1
    print(seraj, dima)
