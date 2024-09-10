# TODO: BackJoon 2178. 미로 탐색 
# NOTE: 사방향으로 가능한 길을 찾아가는 방법이 최단 거리가 될까?

# 미로의 행열 받아오기 -> miro라는 리스트에 좌표(0,1) 정보 저장
# -> 좌표의 방문 정보를 저장하는 리스트 생성 

# 최단 경로를 구하는 BFS 함수 정의

def bfs(si,sj,fi,fj):
    q =[]
    q.append((si,sj))
    # miro 좌표에 방문 정보 저장 
    visited = [[0]*M for _ in range(N)] 
    visited[si][sj] = 1
    
    while q:
        ci,cj = q.pop(0)
        if (ci,cj) == (fi,fj):
            return visited[ci][cj]
        
        for di,dj in (-1,0),(1,0),(0,-1),(0,1):
            ni = ci + di
            nj = cj + dj
            if 0<=ni <N and 0<=nj <M and visited[ni][nj]==0 and miro[ni][nj]==1 :
                q.append((ni,nj))
                visited[ni][nj] = visited[ci][cj] + 1
    


N,M = map(int, input().split(' '))

# 입력받은 좌표 정보 miro에 저장
miro = []
for i in range(N):
    temp = list(map(int, input()))
    miro.append(temp)


# bfs 함수에 시작 좌표와 목적 좌표 전달
answer = bfs(0,0,N-1,M-1)
print(answer)