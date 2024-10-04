# 1️⃣ 깊이 /너비 우선 탐색
# [1] 타겟넘버
# 종료 시점 : numbers가 끝날 때 
# return +1 : 종료 시점에서 타겟의 값과 같을 때.

def DFS (numbers, target,idx, sum_idx):
    if idx == len(numbers): # 모든 수 연산 끝날 때
        if sum_idx == target:
            return 1
        else:
            return 0
    else:
        count = 0 
        count += DFS (numbers, target,idx+1, sum_idx+numbers[idx])
        count += DFS (numbers, target,idx+1, sum_idx-numbers[idx])
        return count

def solution(numbers, target):
    sol_count = 0
    sol_count = DFS (numbers, target,0, 0)
    print(sol_count)
    return DFS (numbers, target,0, 0)
solution([4, 1, 2, 1],2)

# 2️⃣ 해시

# 3️⃣ 정렬

# 4️⃣ 완전 탐색

# 5️⃣ 스택 / 큐

# 6️⃣ 힙 (Heap)

# 7️⃣ 동적 계획법
# 8️⃣ 그래프
# 9️⃣ 이분 탐색
# 1️⃣0️⃣ 탐욕법