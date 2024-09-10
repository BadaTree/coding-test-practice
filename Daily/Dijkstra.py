# TODO: Dijkstra Algorithm에 대해 배워보자 

### 개념 정리 



### 예제 문제 풀이
# [1] 특정 거리의 도시 찾기: 
# https://www.acmicpc.net/problem/18352

from collections import deque
import sys

def find_distance_k(n, m, k, x, roads):
    # 그래프를 인접 리스트로 표현
    graph = [[] for _ in range(n + 1)]
    for a, b in roads:
        graph[a].append(b)
    
    # 거리 정보를 저장할 리스트 초기화
    distance = [-1] * (n + 1)
    distance[x] = 0
    
    # BFS 구현을 위한 큐 초기화
    queue = deque([x])
    
    while queue:
        current = queue.popleft()
        
        for neighbor in graph[current]:
            if distance[neighbor] == -1:  # 방문하지 않은 도시
                distance[neighbor] = distance[current] + 1
                queue.append(neighbor)
    
    # 최단 거리가 K인 도시를 찾기
    result = []
    for i in range(1, n + 1):
        if distance[i] == k:
            result.append(i)
    
    # 결과 출력
    if result:
        result.sort()
        for city in result:
            print(city)
    else:
        print(-1)

# 입력 예시
input = sys.stdin.read().splitlines()
N,M,K,X = map(int, input[0].split(' '))
roads = [(int(i[0]),int(i[2])) for i in input[1:]]

# 함수 호출
find_distance_k(N,M,K,X ,roads)


# [2] 지름길:  
# https://www.acmicpc.net/problem/1446 

# [3] 녹색 옷 입은 애가 젤다지?: 
# https://www.acmicpc.net/problem/4485

# [4] 파티: 
# https://www.acmicpc.net/problem/1238