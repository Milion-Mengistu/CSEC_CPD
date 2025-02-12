def solve():
    n = int(input())
    ans = 0
    for i in range(n):
        check = list(map(int ,input().split()))
        x = check.count(1)
        if x >= 2 :
            ans += 1
    print(ans)
solve()