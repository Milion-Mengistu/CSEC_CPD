def magnet():
    n = int(input())
    magnets = []
    for i in range(n):
        magnets.append(input())
    count = 0
    for i in range(n-1):
        if magnets[i] != magnets[i+1]:
            count += 1
    print(count+1)
magnet()