def blacksquare():

    n = list(map(int, input().split()))
    s = input()
    ans = 0
    for i in s:
        ans += n[int(i)-1]

    print(ans)
blacksquare()


    
   