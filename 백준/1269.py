import sys

A,B = map(int, sys.stdin.readline().split())

set_A = set(map(int,sys.stdin.readline().split()))
set_B = set(map(int,sys.stdin.readline().split()))

print(len((set_A-set_B)|(set_B-set_A)))