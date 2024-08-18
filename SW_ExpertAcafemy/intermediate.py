# [ ] Exhaustive Search : Baby-gin Game

# [ ] Greedy 알고리즘

# [ ] sort 알고리즘( 버블, 카운팅)
# 버블(O(n^2), 카운팅O(N+K))

#  4828. [파이썬 S/W 문제해결 기본] 1일차 - min max

# [입력]

# 첫 줄에 테스트 케이스의 수 T가 주어진다. ( 1 ≤ T ≤ 50 )

# 각 케이스의 첫 줄에 양수의 개수 N이 주어진다. ( 5 ≤ N ≤ 1000 )

# 다음 줄에 N개의 양수 ai가 주어진다. ( 1 ≤ ai≤ 1000000 )

# [출력]

# 각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.

T = int(input())

# 테스트 케이스 수만큼 입력 받고, 계산하기

for i in range(T):
    t = int(input())
    values = list(map(int,input().split(' ')))
 
    max_val = max(values)
    min_val = min(values)
    print(f"#{i+1} {max_val-min_val}")