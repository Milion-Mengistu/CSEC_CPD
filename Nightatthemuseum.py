def nightatthemuseum():
    s = input()

    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    current = 'a'
    result = 0

    for i in s:
        result += min(abs(alphabet.index(i) - alphabet.index(current)), 26 - abs(alphabet.index(i) - alphabet.index(current)))
        current = i

    print(result)
nightatthemuseum()
