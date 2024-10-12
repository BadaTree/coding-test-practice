# 1️⃣ 깊이 /너비 우선 탐색
# [1] 타겟넘버
# 종료 시점 : numbers가 끝날 때 
# return +1 : 종료 시점에서 타겟의 값과 같을 때.

def DFS(numbers, target, idx, sum_idx):
    if idx == len(numbers):
        if sum_idx == target:
            return 1
        else :
            return 0
    else:
        count = 0
        count += DFS(numbers, target, idx+1, sum_idx + numbers[idx])
        count += DFS(numbers, target, idx+1, sum_idx - numbers[idx])
        return count
def solution(numbers, target):
    answer = 0
    answer = DFS(numbers, target,0,0)
    return answer 

# [2] 게임 맵 최단 거리 
# return 최단거리
# 종료 조건 : 상대팀 방문 / 더 이상 이동할 곳이 없을 때

# ***** DFS 활용한 코드 *****
# 종료조건, 불가능 좌표 조건(맵을 벗어나거나 0인 좌표), 이동 조건으로 분리
# 방문한 좌표는 0으로 바꿔주고 다시 1로  
def DFS(maps, n, m, count, x, y):
    # 목표에 도달했을 때
    if (x, y) == (n-1, m-1):  # 좌표는 0부터 시작하므로 n-1, m-1이 목표 지점입니다.
        return count
    # 경계 바깥이거나 벽(0)에 도달했을 때
    elif x < 0 or x >= n or y < 0 or y >= m or maps[y][x] == 0:
        return 100000  # 큰 값을 반환하여 불가능한 경로로 처리
    else:
        maps[y][x] = 0  # 방문한 곳을 0으로 표시 (다시 방문하지 않도록)
        min_cal = 100000  # 최소 값을 찾기 위한 변수
        
        # 좌 (왼쪽)
        if x - 1 >= 0:
            temp_cal = DFS(maps, n, m, count + 1, x - 1, y)
            if temp_cal < min_cal:
                min_cal = temp_cal
        
        # 우 (오른쪽)
        if x + 1 < n:
            temp_cal = DFS(maps, n, m, count + 1, x + 1, y)
            if temp_cal < min_cal:
                min_cal = temp_cal

        # 상 (위쪽)
        if y - 1 >= 0:
            temp_cal = DFS(maps, n, m, count + 1, x, y - 1)
            if temp_cal < min_cal:
                min_cal = temp_cal

        # 하 (아래쪽)
        if y + 1 < m:
            temp_cal = DFS(maps, n, m, count + 1, x, y + 1)
            if temp_cal < min_cal:
                min_cal = temp_cal

        maps[y][x] = 1  # 백트래킹을 위해 다시 1로 표시
        return min_cal

def solution(maps):
    n, m = len(maps[0]), len(maps)
    answer = DFS(maps, n, m, 1, 0, 0)  # 처음 시작할 때 카운트는 1로 시작
    return answer if answer != 100000 else -1  # 불가능할 경우 -1 반환


# ***** BFS 활용한 코드 *****
from collections import deque

def solution(maps):
    # n: 세로 크기, m: 가로 크기
    n, m = len(maps), len(maps[0])
    
    # 방향 벡터 (상, 하, 좌, 우)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    # BFS 구현을 위한 큐
    queue = deque([(0, 0, 1)])  # 시작 좌표 (0, 0)과 시작 거리 1
    
    # 방문한 곳은 0으로 바꿔서 다시 방문하지 않게 처리
    maps[0][0] = 0
    
    while queue:
        x, y, dist = queue.popleft()
        
        # 목표 지점에 도착한 경우
        if x == n - 1 and y == m - 1:
            return dist
        
        # 4방향 탐색
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            
            # 맵 안에 있고 벽이 아닌 경우
            if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] == 1:
                maps[nx][ny] = 0  # 방문 처리
                queue.append((nx, ny, dist + 1))  # 큐에 다음 위치와 거리를 저장
    
    # 목표 지점에 도달할 수 없는 경우
    return -1

# [3] 네트워크

# NOTE :  다시 풀어야하는 문제 
# 내 코드
def DFS(computers,v, visited):
    visited[v] = True
    
    for i ,network in enumerate(computers[v]):
        if network and not visited[i]:
            DFS(computers,i, visited)
                
    
def solution(n, computers):
    visited = [0]*n
    answer = 0
    for i in range(n):
        # 방문하지 않은 컴퓨터가 있다면 방문
        if not visited[i]:
            DFS(computers,0, visited)
            answer += 1
            
    return answer

# GPT 
def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])  # Path compression
    return parent[x]

def union(parent, rank, a, b):
    rootA = find(parent, a)
    rootB = find(parent, b)

    if rootA != rootB:
        # Union by rank
        if rank[rootA] > rank[rootB]:
            parent[rootB] = rootA
        elif rank[rootA] < rank[rootB]:
            parent[rootA] = rootB
        else:
            parent[rootB] = rootA
            rank[rootA] += 1

def solution(n, computers):
    parent = [i for i in range(n)]  # 부모 초기화
    rank = [0] * n  # 랭크 초기화

    for i in range(n):
        for j in range(i + 1, n):  # 대칭 행렬을 피하기 위해 j는 i+1부터 시작
            if computers[i][j] == 1:
                union(parent, rank, i, j)

    # 서로 다른 부모를 가진 컴퓨터의 수를 세어 네트워크 개수 찾기
    networks = set(find(parent, i) for i in range(n))
    return len(networks)

# 예시 실행
print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))  # 2
print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]))  # 1


# 2️⃣ 해시

# 3️⃣ 정렬
# [1] K번째 수 
def solution(array, commands):
    answer = []
    
    for start,end,k in commands:
        answer.append(sorted(array[start-1:end])[k-1])
    
    return answer

# [2] 가장 큰 수
import itertools

def solution(numbers):
    answer = 0
    # 모든 순열 생성
    permutations_list = list(itertools.permutations(numbers))

    # 각 순열을 문자열로 변환하여 이은 수 저장
    for perm in permutations_list:
        combined_number = int(''.join(map(str, perm)))  # 숫자들을 문자열로 변환하여 결합

        if answer < combined_number:
            answer = combined_number

    return str(answer)

# GPT 
def solution(numbers):
    numbers = list(map(str,numbers))
    numbers.sort(key=lambda x: x*3,reverse= True)
    
    return ''.join(numbers) if numbers != ['0']*len(numbers) else '0'

# [3] H-index

# O(N^2)
def solution(citations):
    result = 0
    for h in range(len(citations)+1,1,-1):
        if len([1 for citation in citations if citation >= h]) == h:
            result = h
            break
    
    return result

# GPT  O(n log n)
def solution(citations):
    citations.sort(reverse=True)  # 인용 횟수를 내림차순으로 정렬
    for i, citation in enumerate(citations):
        if citation <= i:  # 인용 횟수가 인덱스보다 작아지면
            return i  # 그 인덱스가 H-Index
    return len(citations)  # 모든 논문이 인용된 경우

# 다시 풀이 
# 1. 내림 차순으로 정렬 후 0번 부터 인용 횟수와 논문 수 비교 
# 이때, i는 0부터 시작하므로 인덱스 i는 i+1번째 논문 
# 따라서 각 citations[i] = n일 때, n이상인 논문의 수가 i+1개가 됨.
# h_index 조건 n >= i+1 논문을 순서대로 확인하면서, "
# 인용 횟수가 논문 순서보다 작아지는 순간"을 찾고 그 수의 -1

# 4️⃣ 완전 탐색

# 5️⃣ 스택 / 큐

# 6️⃣ 힙 (Heap)
#[1] 더 맵게
import heapq

def solution(scoville, K):
    heapq.heapify(scoville)
    mix_value = 0
    
    while scoville[0] < K :
        if len(scoville) < 2 :
            return -1
        
        first = heapq.heappop(scoville)
        second = heapq.heappop(scoville)
        
        new_scoville = first + (second*2)
        heapq.heappush(scoville,new_scoville)
        
        mix_value += 1
    
    return mix_value
#[3] 이중우선순위 큐
# NOTE: 다시 풀어야하는 문제
# 바다
import heapq

def solution(operations):
    queue = []
    for operation in operations:
        cmd, n = operation.split()
        if cmd == 'I':
            queue.append(int(n))
        elif n == '1':
            max_value = max(queue)
            print(max_value,queue)
            # queue.remove(max_value)
        elif n == '-1':
            print(queue,"**")
            heapq.heapify(queue)
            heapq.heappop(queue)
            print(queue)
    return  queue
    # return [max(queue),min(queue)] if queue else [0,0]
# GPT 
def solution(operations):
    queue = []
    
    for operation in operations:
        cmd, num = operation.split()
        num = int(num)

        if cmd == 'I':
            queue.append(num)
            queue.sort()  # 삽입할 때마다 정렬
        elif cmd == 'D':
            if not queue:
                continue
            if num == 1:
                queue.pop()  # 최댓값 삭제
            elif num == -1:
                queue.pop(0)  # 최솟값 삭제

    # 결과 반환
    if not queue:
        return [0, 0]
    else:
        return [max(queue), min(queue)]

# 예시 실행
print(solution(["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]))  # [0, 0]
print(solution(["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]))  # [333, -45]


# 7️⃣ 동적 계획법
# 8️⃣ 그래프
# 9️⃣ 이분 탐색
# 1️⃣0️⃣ 탐욕법