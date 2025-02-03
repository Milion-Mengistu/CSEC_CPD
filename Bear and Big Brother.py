def solve():
    a , b =  map(int, input().split())
    ycount = 0
    while a <= b:
        ycount += 1
        a *= 3
        b *= 2
    print(ycount)
solve()