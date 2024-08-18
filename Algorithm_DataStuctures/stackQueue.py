# TODO : Stack과 Queue 

# 스택, 백준 10828 
# https://www.acmicpc.net/problem/10828

import sys

def stack_fun(num_list, command):
    if command == "pop":
        return num_list.pop() if num_list else -1
    elif command == "size":
        return len(num_list)
    elif command == "empty":
        return 1 if not num_list else 0
    elif command == "top":
        return -1 if not num_list else num_list[-1]

input = sys.stdin.read().splitlines()
N = int(input[0])
num_list = []

for i in range(1, N + 1):
    command = input[i]
    if command.startswith("push"):
        _, num = command.split()
        num_list.append(int(num))
    else:
        result = stack_fun(num_list, command)
        print(result)


# 단어 뒤집기, 백준 9093
# https://www.acmicpc.net/problem/9093

import sys
input = sys.stdin.readlines()

N = int(input[0])
for i in range(1,N+1):
    words = input[i].strip().split(' ')
    print(' '.join([word[::-1] for word in words]))

# 괄호, 백준 9012
# https://www.acmicpc.net/problem/9012

import sys
input = sys.stdin.readlines()

N = int(input[0])

for i in range(1,N+1):
    ps = input[i].strip()
    pslist = []
    isVps = True
    for j in ps :
        if j == '(':
            pslist.append(j)
        else :
            if not pslist :
                isVps = False
                break
            else :
                pslist.pop()
 
    print("YES" if not pslist and isVps else "NO")


# 스택 수열, 백준 1874
# https://www.acmicpc.net/problem/1874


# 에디터, 백준 1406
# https://www.acmicpc.net/problem/1406

#내가 푼 것 
'''
문제점 분석
deque의 rotate 사용: deque.rotate를 사용하여 커서를 이동하는 방식은 효율적이지 않습니다. 특히, 많은 수의 커서 이동 명령이 있을 때 비효율적입니다.
명령어 처리 로직: 명령어 'B'에서 항상 pop을 사용하는 방식은 커서 위치에 관계없이 항상 오른쪽 끝에서 문자를 제거합니다. 이 부분이 잘못되었습니다.
'''

import sys
from collections import deque

input = sys.stdin.read().strip().splitlines()
msg = deque(input[0])
N = int(input[1])
move = 0

for i in range(2,N+2):
    cmd = input[i].split(' ')
    if cmd[0] == 'L':
        msg.rotate(1)
        move += -1
    elif cmd[0] == 'D':
        msg.rotate(-1)
        move += 1
    elif cmd[0] == 'B':
        msg.pop()
    elif cmd[0] == 'P':
        msg.append(cmd[1])
    print(msg)
msg.rotate(move)
print(''.join(msg))

# GPT가 풀이
import sys
input = sys.stdin.read

data = input().splitlines()
initial_string = data[0]
m = int(data[1])
commands = data[2:]

left_stack = list(initial_string)
right_stack = []

for command in commands:
    if command == "L":
        if left_stack:
            right_stack.append(left_stack.pop())
    elif command == "D":
        if right_stack:
            left_stack.append(right_stack.pop())
    elif command == "B":
        if left_stack:
            left_stack.pop()
    elif command.startswith("P"):
        _, char = command.split()
        left_stack.append(char)

result = "".join(left_stack + right_stack[::-1])
print(result)

# 내가 다시 푼 것 

import sys
from collections import deque

input = sys.stdin.read().strip().splitlines()
initial_string = input[0]
M = int(input[1])
commands = input[2:]

l_stack = deque(initial_string)
r_stack = deque()

for cmd in commands:
    if cmd == 'L' and l_stack:
        r_stack.appendleft(l_stack.pop())
    elif cmd == 'D' and r_stack:
        l_stack.append(r_stack.popleft())
    elif cmd == 'B' and l_stack:
        l_stack.pop()
    elif cmd.startswith('P'):
        _, char = cmd.split()
        l_stack.append(char)

result = ''.join(l_stack) + ''.join(r_stack)
print(result)



# 큐, 백준 10845
# https://www.acmicpc.net/problem/10845

from collections import deque
import sys

input = sys.stdin.readlines()

N = int(input[0].strip())
queue = deque()

for i in range(1, N + 1):
    cmd = input[i].strip().split()
    if cmd[0] == "push":
        queue.append(cmd[1])
    elif cmd[0] == "pop":
        if queue:
            print(queue.popleft())
        else:
            print(-1)
    elif cmd[0] == "size":
        print(len(queue))
    elif cmd[0] == "empty":
        print(1 if not queue else 0)
    elif cmd[0] == "front":
        print(queue[0] if queue else -1)
    elif cmd[0] == "back":
        print(queue[-1] if queue else -1)

        
# 요세푸스, 백준 1158
# https://www.acmicpc.net/problem/1158

from collections import deque

N,K = map(int,input().split(' '))
queue = deque([i for i in range(1,N+1)])
result = []

while queue:
    queue.rotate(-(K-1))
    result.append(queue.popleft())
print('<'+', '.join(map(str,result))+'>')  

# GPT 보완 
from collections import deque

# 입력 받기
N, K = map(int, input().split())

# 1번부터 N번까지 사람들을 큐에 넣기
queue = deque(range(1, N + 1))
result = []

# 요세푸스 순열을 생성하는 과정
while queue:
    # 큐를 K-1번 회전시켜 K번째 사람을 앞으로 이동
    queue.rotate(-(K - 1))
    # 큐에서 K번째 사람을 제거하고 결과에 추가
    result.append(queue.popleft())

# 결과 출력
print('<' + ', '.join(map(str, result)) + '>')  


# 덱, 백준 108866
# https://www.acmicpc.net/problem/10866

from collections import deque
import sys

input = sys.stdin.readlines()

N = int(input[0].strip())
queue = deque()

for i in range(1, N + 1):
    cmd = input[i].strip().split()
    if cmd[0] == "push_front":
        queue.appendleft(cmd[1])
    elif cmd[0] == "push_back":
        queue.append(cmd[1])
    elif cmd[0] == "pop_front":
        if queue:
            print(queue.popleft())
        else:
            print(-1)
    elif cmd[0] == "pop_back":
        if queue:
            print(queue.pop())
        else:
            print(-1)
    elif cmd[0] == "size":
        print(len(queue))
    elif cmd[0] == "empty":
        print(1 if not queue else 0)
    elif cmd[0] == "front":
        print(queue[0] if queue else -1)
    elif cmd[0] == "back":
        print(queue[-1] if queue else -1)