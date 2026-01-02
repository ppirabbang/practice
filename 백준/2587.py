import sys

list_int = [int(sys.stdin.readline()) for _ in range(5)]

list_int.sort()

print(sum(list_int)//5)
print(list_int[2])