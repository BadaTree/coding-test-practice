# [ ] Backtracking에 대해 이해해보자 

# [1] Backtracking

# [2] Backtracking 부분 합
def promising(i,weight,total):
    if ((weight + total >= W) and (weight == W or weight + w[i+1] <= W)):
        return True
    else:
        return False

def sum_of_subsets (i,weight,total):
    n = len(w) -1 
    if promising(i, weight, total):
        if weight == W:
            print(include[1: n+1])
        else:
            include[i+1] = True
            sum_of_subsets(i+1,weight+w[i+1], total- w[i+1])
            include[i+1] = False
            sum_of_subsets(i+1, weight, total - w[i+1])

n = 5
W = 21
w = [0,5,6,10,11,16]
total = sum(w)
include = [False]*(n+1)
print(total)
sum_of_subsets(0,0,total)

# [3] Backtracking N-Queen

# [ ] Backtracking 저자 추천 문제

# Programmers, 피로도 level 2
# https://school.programmers.co.kr/learn/courses/30/lessons/87946
'''
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
'''

# Programmers, N-Queen, level2
# https://school.programmers.co.kr/learn/courses/30/lessons/12952
'''
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
'''

# Programmers, 양궁대회, level2
# https://school.programmers.co.kr/learn/courses/30/lessons/92342
'''
def solution(n, info):
    max_diff = 0
    best_shot = [-1]

    def backtrack(shots, idx, arrows_left):
        nonlocal max_diff, best_shot
        if idx == 11 or arrows_left == 0:
            shots[-1] += arrows_left  # 남은 화살을 0점에 모두 사용
            ryan_score, appeach_score = 0, 0

            for i in range(11):
                if shots[i] > info[i]:
                    ryan_score += 10 - i
                elif info[i] > 0:
                    appeach_score += 10 - i

            score_diff = ryan_score - appeach_score
            if score_diff > 0:
                if score_diff > max_diff or (score_diff == max_diff and shots > best_shot):
                    max_diff = score_diff
                    best_shot = shots[:]
            shots[-1] -= arrows_left  # 남은 화살 초기화
            return

        if arrows_left > info[idx]:  # 현재 점수를 이길 수 있을 때
            shots[idx] = info[idx] + 1
            backtrack(shots, idx + 1, arrows_left - shots[idx])
            shots[idx] = 0

        # 현재 점수를 포기할 때
        backtrack(shots, idx + 1, arrows_left)

    backtrack([0] * 11, 0, n)
    return best_shot
'''