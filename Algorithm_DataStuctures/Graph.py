# [ ] Graph에 대해 이해해보자 

# 스택 구현하기 
stack = []
stack.append(5)
stack.append(2)
stack.append(3)
stack.append(7)
stack.pop()
stack.append(1)
stack.append(4)
stack.pop()
'''
print("Stack 구현예제")
print(stack) # 선입부터 # 최하단 원소부터 
print(stack[::-1]) # 후입부터 # 최상단 원소부터
'''
# 깊이 우선 탐색 스택으로 구현 (선입후출) # 1 2 7 6 8 3 4 5
            
def DFS(graph,v,visited):
    visited[v] = True
    print(v,end=' ')
    
    for i in graph[v]:
        if not visited[i]:
            visited[i] = True
            DFS(graph,i,visited)

# 최단 경로             
# 큐 구현하기 
from collections import deque

def BFS(graph,v,visited):
    queue = deque([v])
    visited_bfs[v] = True
    
    while queue:
        v = queue.popleft()
        print(v,end=' ')
        for i in graph[v]:
            if not visited_bfs[i]:
                queue.append(i)
                visited_bfs[i] = True


graph = [[],
         [2,3,8],
         [1,7],
         [1,4,5],
         [3,5],
         [3,4],
         [7],
         [2,6,8],
         [1,7]
    ]

visited = [False] * 9
visited_bfs = [False] * 9 

# DFS(graph,1,visited)
# print()
# BFS(graph,1,visited_bfs)
queue = deque([])
queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft()
queue.append(1)
queue.append(4)
queue.popleft()
'''
print("queue 구현 예제")
print(queue) # 선입부터
queue.reverse() # 순서 반대로 바꾸기
print(queue) # 후입부터
'''

# 재귀함수 구현하기
# 마치 스택에 쌓듯이 실행 함수들을 차례대로 추가하고, 가장 최근에 실행된부터 종료 
def recursive_function(i):
    # 100번째 호출 했을 때 종료되도록 종료 조건 명시
    if i == 100:
        return 
    print(i,'번째 재귀함수를 호출합니다')
    recursive_function(i+1)
    print(i,'번째 재귀함수를 종료합니다')

# recursive_function(1)

# 재귀함수 예시1 ) 팩토리얼 구현하기
def factorial_iterative(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result
def factorial_recursive(n):
    # 종료 조건 : n이 1이 되었을 때
    if n < 1:
        return 1
    # 반복 조건 : n을 -1하며 차례대로 곱한다
    return n*factorial_recursive(n-1) 
'''
print(f"iterative {factorial_iterative(5)}")
print(f"recursive {factorial_recursive(5)}")
'''
# 재귀함수 예시2 ) 최대 공약수 계산 (유클리드 호제법)
# 192와 162의 공약수구하기

# 기본적인 방법으로 풀이 시간: O(min(a,b)), 공간 : O(1)
def GCD (a,b):
    gcd = 1
    n = min(a,b)
    for i in range(1,n+1):
        if a% i == 0 and b % i == 0 :
            gcd = i
                
    
    return gcd
# print("basic", GCD(192,162))

# 유클리드 호제법 :
def Euclidean(a,b):
    r = a%b
    if r == 0 :
        return b
    return Euclidean(b, r)

# print(f"Euclidean {Euclidean(192,162)}")
# NOTE : 재귀 함수는 반복문을 이용하여 동일한 기능을 구현 가능
# 스택 대신 재귀함수를 이용(재귀함수를 연속적으로 호출하면 컴퓨터 메모리에 내부에 스택 프레임에 쌓여). 
# 재귀함수도 스택처럼 LIFO 나중에 실행된 함수부터 종료된다.


# [1] DFS (Depth-first Search), 스택 자료구조(혹은 재귀함수)를 이용
# 깊이 우선 탐색이라고 부르며 그래프에서 싶은 부분을 우선적으로 탐색하는 알고리즘이다.
# 1. 탐색 시작 노드를 스택에 삽입하고, 방문 처리한다.
# 2. 스택의 최상단의 노드에 방문하지 않은 인접 노드가 있다면, 노드의 값이 가장 작은 '한 개'를 스택에 삽입하고 방문 처리
#    스택의 최상단의 노드에 더이상 방문할 노드가 없다며, 최상단 노드를 꺼낸다.
# 3. 더 이상 2번의 과정을 수행할 수 없을 때까지 반복한다.  

# DFS 메서드 정의 
def dfs(graph, v, visited):
    # 현재 노드를 방문 처리
    visited[v] = True
    print(v, end=' ')
    # 현재 노드의 연결된 다른 노드 중 방문하지 않은 노드를 재귀적으로 방문 
    # 현재 노드에서 더 이상 방문할 노드가 없다면 해당 노드 dfs 종료 (스택에서 pop)
    for i in graph[v]:
        if not visited[i]:
            dfs(graph,i,visited)
        
graph = [
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]
# 각 노드가 방문된 정보를 표현 
visited = [False]* 9 #(노드의 값과 인덱스를 맞춰주기 위해 노드 수 + 1)

# 정의된 DFS 함수 호출
# dfs(graph,1,visited)


# [2] BFS (Breadth-First Search), Queue를 활용
# 너비우선 탐색이라고도 부르며, 그래프에서 시작노드에서 가까운 노드부터 우선적으로 탐색하는 알고리즘
# 1. 탐색 시작 노드를 큐에 삽입하고, 방문 처리를 합니다.
# 2. 큐의 맨 앞 노드를 꺼낸 뒤, 해당 노드의 인접노드 중 방문하지 않은 노드를 '모두' 큐에 삽입하고 방문 처리합니다.
# 3. 더 이상 2번의 과정을 수행할 수 없을 때까지 반복합니다.
'''
from collections import deque

# BFS 메서드 정의
def bfs (graph, start, visited):
    # 큐 구현을 위해 deque 라이브러리 사용
    queue = deque([start])
    # 현재 노드를 방문 처리
    visited[start] = True
    # 큐가 빌 떄까지 반복
    while queue:
        # 큐에서 맨 앞의 노드를 꺼내 출력
        v = queue.popleft()
        print(v,end=' ')
        # 해당 노드에 인접 노드 중 방문하지 않은 노드 '모두' 큐에 삽입
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

          
graph = [
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]
# 각 노드가 방문된 정보를 표현 
visited = [False]* 9 #(노드의 값과 인덱스를 맞춰주기 위해 노드 수 + 1)

# 정의된 DFS 함수 호출
# bfs(graph,1,visited)
'''

# [3] 다익스타라 알고리즘 이해하기
# 현재까지 알고 있던 최단 경로를 계속해서 갱신한다. 
# 현재 직접 연결된 노드들까지 가는 비용에서 다른 노드를 거쳐서 갔을 때의 비용을 갱신해준다.

# 1. 출발 노드를 설정합니다.
# 2. 출발 노드를 기준으로 각 노드의 최소 비용을 저장합니다.
# 3. 방문하지 않은 노드 중에서 가장 비용이 적은 노드를 선택한다.
# 4. 해당 노드를 거쳐서 특정한 노드로 가는 경우를 고려하여 최소 비용을 갱신한다.
# 5. 위 과정에서 3번 ~ 4번을 반복한다.




# [4] 밸만포드 알고리즘 이해하기 






# [ ] 이코테 저자 나동빈 추천 문제 
# https://www.youtube.com/watch?v=7C9RgOcvkvo&list=PLRx0vPvlEmdAghTr5mXQxGpHjWqSz0dgC&t=2s
# 1. 음료수 얼려 먹기 :
# 1. 값이 0인 노드에 방문하여 상하좌우 뚫려 있고 방문 하지 않은 노드를 방문
# 2. 새롭게 방문한 노드에서 또 상하 좌우를 서치하며 연결된 모든 노드를 서치
# 3. 더 이상 연결된 노드가 없을 때 ice +1 
'''
def DFS(x,y ,n,m,graph):
    # 그래프 범위를 넘어가면 바로 False
    if y < 0 or n-1 < y or x < 0 or m-1 < x:
        return False
    # 시작 위치에서 인접한 좌우상하 노드 전체 서치
    if graph[y][x] == 0:
        # 해당 노드 방문 처리
        graph[y][x] = 1
        # 상하좌우 인전 노드 확인, 리턴하지 않으므로 단순히 인접노드 방문 처리용
        DFS(x-1,y ,n,m,graph)
        DFS(x+1,y ,n,m,graph)
        DFS(x,y-1 ,n,m,graph)
        DFS(x,y+1 ,n,m,graph)
        # 인접한 모든 노드를 모두 방문 했을 때 하나의 ICE 찾음의 의미 True 반환   
        return True
         
    return False

import sys

# input = sys.stdin.readlines()

n,m = map(int,input[0].strip().split())
ICE = 0

# 그래프 생성
graph = []
for i in range(1,n+1):
    graph.append(list(map(int,input[i].strip())))

# 차례대로 노드를 방문해서 상하좌우 방문하지 않고, 값이 0인 노드 있는지 연결 확인
# 연결된 노드가 있다면 0 -> 1로 방문처리하고, 해당 노드로 이동하여 상하좌우 확인

for y in range(n):
    for x in range(m):
        # ICE 체크 기준 첫 시작 노드가 방문처리 되었나 ? + 1
        # but 이어서 인전노드들의 재귀함수 반환값은 이용하지 않으므로 단순히 방문처리용
        if DFS(x,y ,n,m,graph):
            ICE += 1
print(ICE)
'''
# 2. 미로 탈출
 
# BFS 구현 
def bfs(x,y):
    # 큐 구현
    queue = deque()
    queue.append((x,y))
    
    #큐가 빌 때까지 반복하기
    while queue :
        x,y = queue.popleft()
        # 현재 위치에서 4가지 방향으로의 위치 확인 
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 미로 찾기 공간을 벗어난 경우 무시 
            if nx < 0 or nx >= n or ny < 0 or ny >= m :
                continue
            # 괴물 위치인 경우 무시
            if graph[nx][ny] == 0 :
                continue
            # 해당 노드를 처음 방문하는 경우에만 최단 거리 기록 
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx,ny))
    
    # 가장 오른쪽 아래까지의 최단 거리 반환
    return graph[n-1][m-1]


from collections import deque

# N,M을 공백을 기준으로 구분하여 입력 받기
n,m = map(int,input().split())
# 2차원 리스트의 맵 정보 입력 받기
graph = []
for i in range(n):
    graph.append(list(map(int,input())))
    
# 이동할 네 가지 방향 정의 (상, 하, 좌, 우)
dx = [-1,1,0,0]
dy = [0,0,-1,1]

# BFS를 수행한 결과 출력
print(bfs(0,0))
        


# [ ] 저자 추천 문제
# [1] 전력망을 둘로 나누기(level2, programmers)
# https://programmers.co.kr/learn/courses/30/lessons/86971
# [2] 양과 늑대 (level3, programmers)
# https://programmers.co.kr/learn/courses/30/lessons/92343
# [3] 미로탈출 (level2, progrmmers)
# https://school.programmers.co.kr/learn/courses/30/lessons/159993

# [ ] 내가 찾은 추천 문제
# [1] 7576번: 토마토 (골드 5)
# https://www.acmicpc.net/problem/7576


# [1] 1,2,3 더하기 (실버3)
# https://www.acmicpc.net/problem/9095


# [2] 가장 긴 바이토닉 부분 수열(골드5)
# https://www.acmicpc.net/problem/11054