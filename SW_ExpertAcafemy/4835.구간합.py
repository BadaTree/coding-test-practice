# TODO : 4835. [파이썬 S/W 문제해결 기본] 1일차 - 구간합

T = int(input()) # 테스트 케이스 개수 T

N,M = map(int,input().split(' ')) # 테스트케이스의 첫 줄에 정수의 개수 N과 구간의 개수 M

for i in range(1,T+1):
    num_list = list(map(int,input().split(' '))) # N개의 정수 ai가 주어진다

    # num_list를 오를차순으로 정렬
    num_list.sort()

    # 최댓값은 가장 큰 인덱스부터 M개 , 최솟값은 가장 작은 인덱스부터 M개 

    result = sum(num_list[-M:]) - sum(num_list[0:M])

    print(f"#{i} {result}") 
