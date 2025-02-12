def games():

    n = int(input())
    games = []
    for i in range(n):
        games.append(list(map(int, input().split())))
    ans = 0
    for i in range(n):
        for j in range(n):
            if games[i][0] == games[j][1]:
                ans += 1
    print(ans)
games()