# TODO: 4834. [파이썬 S/W 문제해결 기본] 1일차 - 숫자 카드

# [입력]
 

# 첫 줄에 테스트 케이스 개수 T가 주어진다.  ( 1 ≤ T ≤ 50 )

# 다음 줄부터 테스트케이스의 첫 줄에 카드 장수 N이 주어진다. ( 5 ≤ N ≤ 100 )

# 다음 줄에 N개의 숫자 ai가 여백없이 주어진다. (0으로 시작할 수도 있다.)  ( 0 ≤ ai ≤ 9 ) 

 

# [출력]
 

# 각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 가장 많은 카드의 숫자와 장 수를 차례로 출력한다.

T = int(input()) # 케이스 갯수 입력 받기

# 케이스마다 카드 수 list에 입력받기
for i in range(1,T+1):
    N = int(input())
    cards = [0]*10
    temp = list(map(int,input()))
    
    # 0~9까지의 빈도 수를 담는 list를 생성
    for j in temp:
        cards[j] += 1
    
    max_num = max(cards)
    
    max_index = max(i for i, v in enumerate(cards) if v == max_num) 
    print(f"#{i} {max_index} {max_num} ")