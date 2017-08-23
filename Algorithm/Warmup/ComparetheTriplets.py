#!/bin/python3

import sys

def solve(a0, a1, a2, b0, b1, b2):
    # Complete this function
    alice = [a0,a1,a2]
    bob = [b0,b1,b2]
    a,b=0,0
    for i in range(3):
        if alice[i]>bob[i]:
            a = a+1
        elif alice[i]<bob[i]: 
            b = b+1
    return str(a)+str(b) 
    
a0, a1, a2 = input().strip().split(' ')
a0, a1, a2 = [int(a0), int(a1), int(a2)]
b0, b1, b2 = input().strip().split(' ')
b0, b1, b2 = [int(b0), int(b1), int(b2)]
result = solve(a0, a1, a2, b0, b1, b2)
print (" ".join(map(str, result)))


