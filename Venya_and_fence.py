def venya_fence(n, h, heights) -> int:
    w = 0
    for height in heights:
        if height > h:
            w += 2
        else:
            w += 1
    return w


n, h = map(int, input().split())
heights = list(map(int, input().split()))
result = venya_fence(n, h, heights)
print(result)