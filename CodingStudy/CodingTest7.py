# TODO: 7.3 스터디 공통문제 



# [ ] 특정 거리의 도시 찾기: 실버 2
# https://www.acmicpc.net/problem/18352

# [ ] 지름길:  실버 1 
# https://www.acmicpc.net/problem/1446 


# [ ]녹색 옷 입은 애가 젤다지? 골드5: 
# https://www.acmicpc.net/problem/4485

# 최단경로가 아니라 루피를 최소한으로 잃는 경로 찾기
# 0~N-1 좌표만 이동 가능, 


import heapq
import sys
input = sys.stdin.read


# 상, 하, 좌, 우 네 방향을 나타내는 델타값
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dijkstra(N, cave):
    # 최소 비용을 저장하는 배열
    dist = [[float('inf')] * N for _ in range(N)]
    dist[0][0] = cave[0][0]

    # 우선순위 큐 사용
    pq = [(cave[0][0], 0, 0)]  # (비용, x, y)
    while pq:
        current_dist, x, y = heapq.heappop(pq)
        
        # 이미 처리된 적 있는 노드는 무시
        if current_dist > dist[x][y]:
            continue
        
        # 네 방향으로 이동
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                next_dist = current_dist + cave[nx][ny]
                if next_dist < dist[nx][ny]:
                    dist[nx][ny] = next_dist
                    heapq.heappush(pq, (next_dist, nx, ny))

    # 목적지의 최소 비용 반환
    return dist[N-1][N-1]

input_data = input().strip().split()
index = 0
problem_number = 1
    
while True:
    N = int(input_data[index])
    if N == 0:
        break
    index += 1
        
    cave = []
    for i in range(N):
        cave.append(list(map(int, input_data[index:index + N])))
        index += N
        
    result = dijkstra(N, cave)
    print(f"Problem {problem_number}: {result}")
    problem_number += 1


# [ ] 파티 골드3:
# https://www.acmicpc.net/problem/1238

