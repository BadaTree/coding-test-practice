

# [ ] 트리 관련 코테 문제

# [1] 트리 순회(백준 1991, 실버 1)
# https://www.acmicpc.net/problem/1991
'''
class Node:
    def __init__(self, value, left, right):
        self.value = value
        self.left = left
        self.right = right

def pre_order(node):
    print(node.value, end='')
    if node.left != None:
        pre_order(tree[node.left])
    if node.right != None:
        pre_order(tree[node.right])

def in_order(node):
    if node.left != None:
        in_order(tree[node.left])
    print(node.value, end='')
    if node.right != None:
        in_order(tree[node.right])  # 여기서 pre_order가 아닌 in_order를 호출해야 합니다.

def post_order(node):
    if node.left != None:
        post_order(tree[node.left])
    if node.right != None:
        post_order(tree[node.right])
    print(node.value, end='')

N = int(input())
tree = {}

for i in range(N):
    value, left, right = input().split()
    if left == '.':
        left = None
    if right == '.':
        right = None
    tree[value] = Node(value, left, right)

pre_order(tree['A'])
print()
in_order(tree['A'])
print()
post_order(tree['A'])
print()
'''

# [2] 트리 부모 찾기 (백준 11725, 실버2)
# https://www.acmicpc.net/problem/11725
class Node :
    def __init__(self, parent,left,right):
        self.parent = parent
        self.left = left
        self.right = right

N = int(input())
tree={}

for i in range(N-1):
    a,b = input().split()
    
    # 트리에 없다면 노드 생성
    if a not in tree:
        tree[a] = Node(None,None,None)
    if b not in tree:
        tree[b] = Node(None,None,None)  

    # a,b의 부모 자식 관계 정하기
    # a가 부모인 경우
    if a == '1' or tree[a].parent is not None:
        # a의 자식노드에 b 추가
        if tree[a].left is None:
            tree[a].left = b
        else:
            tree[a].right = b
        # b의 부모 노드에 a 추가
        tree[b].parent = a
       
    # b가 부모인 경우
    elif b =='1' or tree[b].parent is not None:
        # b의 자식 노드에 a 추가
        if tree[b].left is None:
            tree[b].left = a
        else:
            tree[b].right = a
        # a의 부모 노드에 b 추가
        tree[a].parent = b

# 결과 확인을 위해 트리 구조 출력
for node, data in tree.items():
    print(f"Node {node}: Parent = {data.parent}, Left = {data.left}, Right = {data.right}")

for i in range(2,N+1):
    print(tree[str(i)].parent)

# GPT 풀이 
import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
tree = [[] for _ in range(N + 1)]
parents = [0] * (N + 1)

for _ in range(N - 1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

def bfs(root):
    queue = deque([root])
    while queue:
        node = queue.popleft()
        for neighbor in tree[node]:
            if parents[neighbor] == 0:
                parents[neighbor] = node
                queue.append(neighbor)

bfs(1)

for i in range(2, N + 1):
    print(parents[i])
    
# [3] 트리의 지름 (백준 1167, 골드 2)
# https://www.acmicpc.net/problem/1167

# [4] 트리의 지름 (백준 1967, 골드 4)
# https://www.acmicpc.net/problem/1967

# [5] 트리(백준 1068, 골드 5)
# https://www.acmicpc.net/problem/1068

# [6] 이진 검색 트리 (백즌 5639, 골드4)
# https://www.acmicpc.net/problem/5639

# [7] 상근이의 여행 (백준 9372, 실버4)
# https://www.acmicpc.net/problem/9372

# [8] 전화번호 목록 (백준 5051, 골드4)
# https://www.acmicpc.net/problem/5052

# [9] 트리의 순회 (백준 2263, 골드 1)
# https://www.acmicpc.net/problem/2263
