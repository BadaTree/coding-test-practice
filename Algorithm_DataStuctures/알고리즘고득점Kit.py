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

# DFS 활용한 코드
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





# 2️⃣ 해시

# 3️⃣ 정렬

# 4️⃣ 완전 탐색

# 5️⃣ 스택 / 큐

# 6️⃣ 힙 (Heap)

# 7️⃣ 동적 계획법
# 8️⃣ 그래프
# 9️⃣ 이분 탐색
# 1️⃣0️⃣ 탐욕법