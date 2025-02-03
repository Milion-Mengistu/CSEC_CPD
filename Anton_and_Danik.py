def solve():
    n = int(input())
    s = input().upper()
    if len(s) > n or len(s) < n:
        return 
    A = s.count("A")
    D = s.count("D")
    if A > D : 
        print("Anton")
    elif A == D :
        print("Friendship")
    
    else:
        print("Danik")
solve()
