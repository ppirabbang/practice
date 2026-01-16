import sys
from collections import deque

# 빠른 입출력을 위해 사용
input = sys.stdin.readline

N = int(input())
dq = deque()

for _ in range(N):
    command = input().split()
    cmd_type = command[0]

    if cmd_type == '1':
        # 1 X: 정수 X를 덱의 앞에 넣는다.
        dq.appendleft(int(command[1]))
        
    elif cmd_type == '2':
        # 2 X: 정수 X를 덱의 뒤에 넣는다.
        dq.append(int(command[1]))
        
    elif cmd_type == '3':
        # 3: 덱에 정수가 있다면 맨 앞의 정수를 빼고 출력한다. 없다면 -1
        if dq:
            print(dq.popleft())
        else:
            print(-1)
            
    elif cmd_type == '4':
        # 4: 덱에 정수가 있다면 맨 뒤의 정수를 빼고 출력한다. 없다면 -1
        if dq:
            print(dq.pop())
        else:
            print(-1)
            
    elif cmd_type == '5':
        # 5: 덱에 들어있는 정수의 개수를 출력한다.
        print(len(dq))
        
    elif cmd_type == '6':
        # 6: 덱이 비어있으면 1, 아니면 0을 출력한다.
        if not dq:
            print(1)
        else:
            print(0)
            
    elif cmd_type == '7':
        # 7: 덱에 정수가 있다면 맨 앞의 정수를 출력한다. 없다면 -1
        if dq:
            print(dq[0])
        else:
            print(-1)
            
    elif cmd_type == '8':
        # 8: 덱에 정수가 있다면 맨 뒤의 정수를 출력한다. 없다면 -1
        if dq:
            print(dq[-1])
        else:
            print(-1)