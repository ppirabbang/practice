import sys

def canto(n):
  if(n == 0):
    return "-"
  else:
    return canto(n-1) + 3 ** (n-1) * " " + canto(n-1)
  
while(line := sys.stdin.readline()):
  N = int(line)
  print(canto(N))