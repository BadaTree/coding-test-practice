#TODO: [BackJoon 1260] DFS와 BFS

def dfs(graph,v,visited):
    visited[v] = True
    dfs_result = str(v)+ ' '
    print(v, end=' ')
    
    for i in graph[v]:
        if not visited[i]:
            dfs(graph,i,visited)
    return dfs_result

from collections import deque

def bfs(graph,start,visited):
    queue = deque([start])
    visited[start] = True
 
    while queue:
        v = queue.popleft()
        print(v, end=' ')

        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] =True
                
    return bfs_result

N,M,V = map(int,input().split(' ') )
dfs_result = ''
bfs_result = ''

# 주어진 간선을 바탕으로 그래프 생성
graph = [[] for _ in range(N+1)]

for i in range(M):
    p1,p2 = map(int,input().split(' '))
    graph[p1].append(p2)
    graph[p2].append(p1)

    
for i in range(N):
    graph[i].sort()

# 정점의 방문 기록을 저장하는 리스트 생성
visited=[False]*(N+1)
dfs(graph,V,visited)
# 정점의 방문 기록을 저장하는 리스트 생성
visited=[False]*(N+1)
bfs(graph,V,visited)
print()


