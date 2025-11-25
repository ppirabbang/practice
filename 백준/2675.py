import sys

count = int(sys.stdin.readline())

for i in range(count):
    a, b = sys.stdin.readline().split() 

    a = int(a)
    for k in range(len(b)):
        print(b[k] * a, end="")
    print()
