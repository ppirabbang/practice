import sys

a = int(sys.stdin.readline())
b = int(sys.stdin.readline())
c = int(sys.stdin.readline())
sum = a + b + c

if(a == 60 and b == 60 and c == 60):
  print("Equilateral")
elif(sum == 180 and (a == b or a == c or b == c)):
  print("Isosceles")
elif(sum == 180 and (a != b and b != c and a != c)):
  print("Scalene")
elif(sum != 180):
  print("Error")