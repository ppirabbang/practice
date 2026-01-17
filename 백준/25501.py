import sys

def recursion(s, l, r):
    global cnt
    cnt += 1
    if l >= r: return 1
    elif s[l] != s[r]: return 0
    else: return recursion(s, l+1, r-1)

def isPalindrome(s):
    global cnt
    cnt = 0
    return recursion(s, 0, len(s)-1)

N = int(sys.stdin.readline())
cnt = 0

for i in range(N):
    str_ = sys.stdin.readline().rstrip()
    print(f"{isPalindrome(str_)} {cnt}" )
