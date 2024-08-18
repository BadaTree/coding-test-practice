# TODO: BackJoon 2060. 바이러스 

def dfs(start):
    global count 
    
    v = start
    visited[v] = 1
    count += 1
    
    for i in graph[v]:
        if not visited[i]:
            dfs(i)
    return count-1


N = int(input())
M = int(input())

# 인접 정보 리스트 생성
graph = [[] for i in range(N+1)]
for i in range(M):
    c1,c2 = map(int,input().split(' '))
    graph[c1].append(c2)
    graph[c2].append(c1)

count = 0
# 방문기록 리스트 생성
visited = [0]*(N+1)

answer = dfs(1)
print(answer)