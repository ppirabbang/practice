import sys

A,B,C = map(int, sys.stdin.readline().split())

def dac(a,b,c):
  if(b == 1):
    return a % c
  else:
    if(b %2 == 0):
      return (dac(a,b//2,c) ** 2) % c
    else:
      return ((dac(a,b//2,c) **2) * a) % c
    
print(dac(A,B,C))