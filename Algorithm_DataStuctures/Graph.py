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

# [ ] 최단 경로 문제 마스터하기 !!
# 최단 경로 문제 CASE
# 1. 한 지점에서 다른 한 지점까지의 최단 경로 
# 2. 한 지점에서 다른 모든 지점까지의 최단 경로 
# 3. 모든 지점에서 다른 모든 지점까지의 최단 경로 

# 각 지점은 (나라, 지역, 건물)은 그래프에서 '노드'로 표현
# 지점 간 연결된 도로(통로, 도로, 길..)는 그래프에서 간선으로 표현

# [3] 다익스타라 알고리즘 이해하기
# 특정한 노드에서 출발하여 다른 모든 노드로 가는 최단 경로를 계산한다.
# 다익스트라 최단 경로 알고리즘은 음의 간선이 없을 때 정상 동작 -> 현실에선 음의 간선 없음 -> 현실에서 활용하기 유용
# 다익스트라 알고리즘은 그리디 알고리즘에 분류 됨. 왜? 매 상황 가장 비용이 적은 노드를 선택하고, 갱신하는 과정이 그리디 알고리즘과 같음.

# 다익스트라 알고리즘 동작 과정 
# 1. 출발 노드 설정
# 2. 최단 거리 테이블 초기화 (자기 자신은 0, 나머지 노드는 모두 무한대로 설정)
# 3. 방문하지 않은 노드 중에서 최단 거리가 가장 짧은 노드를 선택합니다.
# 4. 해당 노드를 거쳐 다른 노드로 가는 비용을 계산하여 최단 거리 테이블을 갱신합니다.
# 위 과정까지 거치면 최단 거리까지 알 수 있음 (최단 거리의 경로는 각 단계에서 최단 경로들의 연결)
# 5. 위 과정에서 3번과 4번을 반복합니다.

# 다익스트라 알고리즘 특징 
# 매 상황에서 방문하지 않은, 가장 비용이 적은 노드를 선택해 임의의 과정을 반복한다 -> 그리디 알고리즘
# 한 번 방문 처리된 노드의 최단 거리는 고정되어 더 이상 바뀌지 않는다.
# -> 한 단계당 하나의 노드에 대한 최단 거리를 확실히 찾는 것으로 이해할 수 있다.
# 다익스트라 알고리즘을 수행한 후에는 최단거리에 대한 정보만 ! 최단 경로를 구하려면 추가적 기능을 더 넣어야한다.

# 구현 Tip (~ 15):
# 단계마다 방문하지 않은 노드 중에서 최단 거리가 가장 짧은 노드를 선택하기 위해 
# 매 단계마다 1차원 테이블의 모든 원소를 확인한다.
'''
import sys 
input = sys.stdin.readline
INF = int(1e9) # 무한을 의미하는 값으로 10억을 설정

# 노드의 개수, 간선의 개수를 입력 받기 
n,m = map(int,input().split())
# 시작 노드 번호를 입력 받기
start = int(input()) 
# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트를 만들기
graph = [[] for i in range(n+1)]
# 방문한 적이 있는지 체크하는 목적의 리스트를 만들기
visited = [False] * (n+1)
# 최단 거리 테이블을 모두 무한으로 초기화
distance = [INF] * (n+1)

# 모든 간선 정보를 입력 받기
for _ in range(m):
    a,b,c = map(int,input().split())
    # a번 노드에서 b번 노드로 가는 비용이 c라는 의미 
    graph[a].append((b,c))

# 방문하지 않은 노드 중에서, 가장 최단 거리가 짧은 노드의 번호를 반환
def get_smallest_node():
    min_value = INF
    index = 0 # 가장 최단 거리가 짧은 노드(인덱스)
    for i in range(1,n+1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
    return index

def dijkstra(start):
    # 시작 노드에 대해서 초기화
    distance[start] = 0
    visited[start] = True
    for j in graph[start]:
        distance[j[0]] = j[1]
    
    # 시작 노드를 제외한 전체 n-1 개의 노드에 대해 반복
    for i in range(n-1):
        # 현재 최단거리가 가장 짧은 노드를 꺼내서, 방문 처리
        now = get_smallest_node()
        visited[now] = True
        # 현재 노드와 연결된 다른 노드를 확인
        for j in graph[now]:
            cost = distance[now] + j[1]
            # 현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[j[0]]:
                distance[j[0]] = cost

# 다익스트라 알고리즘을 수행
dijkstra(start)

# 모든 노드로 가기 위한 최단 거리를 출력
for i in range(1,n+1):
    # 도달할 수 없는 경우, 무한이라고 출력
    if distance[i] == INF :
        print("INFINITY")
    # 도달할 수 있는 경우 거리를 출력
    else:
        print(dijkstra[i])
'''
# [3] 힙 라이브러리 활용해서 다익스트라 구현하기 
import heapq

# 오름차순 힙 정렬(Heap Sort)
def heapsort(iterable):
    h = []
    result = []
    # 모든 원소를 파례대로 힙에 삽입
    for vaule in iterable:
        heapq.heappush(h,vaule)
    # 힙에 삽입된 모든 원소를 차례대로 꺼내어 담기
    for i in range(len(h)):
        result.append(heapq.heappop(h))
    return result

result = heapsort([1,3,5,7,9,2,4,6,8,0])
print(result)

# [4] 플로이드 워셜 알고리즘 이해하기

# [5] 밸만포드 알고리즘 이해하기 






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