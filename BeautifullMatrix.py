def solve():
    n = 5
    for i in range(n):
        check = list(map(int ,input().split()))
        if len(check) == 5:
            for j in range(n):
                if check[j] == 1:
                    print(abs(i-2) + abs(j-2))
                    break
    
solve()
    
        
    