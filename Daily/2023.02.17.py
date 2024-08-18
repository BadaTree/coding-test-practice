# 구현 : 머릿 속에 있는 알고리즘을 소스코드로 바꾸는 과정
# ex: problem -> thinking -> solution

# 구현 문제란??
# 풀이는 떠올리기 쉬우나 소스 코드로 옮기는게 어려운 문제

# 일반적으로 알고리즘 문제에서의 2차원 공간은 행렬의 의미로 사용됩니다.

# for i in range(5):
#     for j in range(5):
    #     print('(',i,',',j, ')', end ='')
    # print()

# 시뮬레이션 및 완전 탐색 문제에서는 2차원 공간에서의 방향 벡터가 자주 활용됩니다.
# 동, 북, 서 , 남
dx = [0,-1,0,1]
dy = [1,0,-1,0]

# 현재 위치
x,y = 2,2

for i in range(4):
    # 다음 위치
    nx = x + dx[i]
    ny = y + dy[i]
    # print(nx,ny)


# ******** 예시 문제 : 상하 좌우 문제 ********
N = int(input())
plan = input().split()
x,y = 1,1

# # L : y - 1
# # R : y + 1
# # U : x - 1
# # D : x + 1
dx = [0,0,-1,1]
dy = [-1,1,0,0]
move_types = ['L','R','U','D']

# 이동 계획을 하나씩 확인하기
for i in range(len(plan)):
    for j in range(4):
        if plan[i] == move_types[j]:
            nx = x + dx[j]
            ny = y + dy[j]
    # 공간을 벗어나는 경우는 무시함.
    if nx < 1 or nx > N or ny < 1 or ny > N:
        continue
    # 이동 수행
    x,y = nx, ny

print(x,y)