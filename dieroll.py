import math

def die_roll(y, w):
    max_val = max(y, w)  
    favorable = 6 - max_val + 1  
    gcd_val = math.gcd(favorable, 6)  
    print(f"{favorable // gcd_val}/{6 // gcd_val}")  
y, w = map(int, input().split())
die_roll(y, w)
