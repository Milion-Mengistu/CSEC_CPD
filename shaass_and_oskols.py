def shaass_and_oskols(wires, shots):
    for shot in shots:
        wire, bird = shot
        wire -= 1  # Convert to zero-based index
        if wire > 0:
            wires[wire - 1] += bird - 1
        if wire < len(wires) - 1:
            wires[wire + 1] += wires[wire] - bird
        wires[wire] = 0
    return wires


n = int(input())
wires = list(map(int, input().split()))
m = int(input())
shots = [tuple(map(int, input().split())) for _ in range(m)]

result = shaass_and_oskols(wires, shots)
print(' '.join(map(str, result)))