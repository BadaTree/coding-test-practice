# [ ] 알고리즘 기초 1
# https://blog.naver.com/zzzxxx3166/223517272663

# [1] 스택
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


# [2] 단어 뒤집기
import sys
input = sys.stdin.readlines()

N = int(input[0])
for i in range(1,N+1):
    words = input[i].strip().split(' ')
    print(' '.join([word[::-1] for word in words]))
# [3] 괄호
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

# [4] 스택 수열
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


# [5] 에디터
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

# [6] 조퍼스 문제
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
 