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



# 4️⃣ 완전 탐색

# 5️⃣ 스택 / 큐

# 6️⃣ 힙 (Heap)

# 7️⃣ 동적 계획법
# 8️⃣ 그래프
# 9️⃣ 이분 탐색
# 1️⃣0️⃣ 탐욕법