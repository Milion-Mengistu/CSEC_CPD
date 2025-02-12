def colorful_stones(s, t):
    position = 0
    for char in t:
        if char == s[position]:
            position += 1
        if position == len(s):
            break
    return position + 1

s = input().strip()
t = input().strip()
print(colorful_stones(s, t))