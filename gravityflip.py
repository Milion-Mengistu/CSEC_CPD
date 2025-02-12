def solve():
    n =  int(input())
    check = list(map(int ,input().split()))
    if len(check) == n:
        check.sort()
        print(*check)
    

solve()