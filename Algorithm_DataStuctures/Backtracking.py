# [ ] Backtracking에 대해 이해해보자 

# [1] Backtracking

# [2] Backtracking 부분 합

# [3] Backtracking N-Queen

# [ ] Backtracking 저자 추천 문제
# Programmers, 피로도 level 2
# https://school.programmers.co.kr/learn/courses/30/lessons/87946
from itertools import permutations

def solution(k, dungeons):
    max_dungeons = 0
    all_permutations = list(permutations(dungeons))
    
    for perm in all_permutations:
        current_k = k
        explored_count = 0
        for dungeon in perm:
            min_required, fatigue_cost = dungeon
            if current_k >= min_required:
                current_k -= fatigue_cost
                explored_count += 1
            else:
                break
        max_dungeons = max(max_dungeons, explored_count)
    
    return max_dungeons


# Programmers, N-Queen, level2
# https://school.programmers.co.kr/learn/courses/30/lessons/12952
def solution(n):
    def is_safe(queens, row, col):
        for r in range(row):
            if queens[r] == col or \
               queens[r] - r == col - row or \
               queens[r] + r == col + row:
                return False
        return True
    
    def solve(queens, row):
        if row == n:
            return 1
        count = 0
        for col in range(n):
            if is_safe(queens, row, col):
                queens[row] = col
                count += solve(queens, row + 1)
        return count
    
    queens = [-1] * n
    return solve(queens, 0)


# Programmers, 양궁대회, level2
# https://school.programmers.co.kr/learn/courses/30/lessons/92342