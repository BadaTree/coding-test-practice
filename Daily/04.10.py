# TODO: 구현 마스터하기 
#[이것이 코딩테스트이다. 구현](https://www.youtube.com/watch?v=puH2p1CQEg4)

N = int(input())
plans = input().split()

x = 1
y = 1
# L R U D
dx = [0,0, -1,1]
dy = [-1, 1, 0,0]
type = ['L', 'R','U','D']


for plan in plans :
    for i in range(len(type)):
        if plan == type[i]:
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < N or ny < N or nx > 1 or ny > 1:
                x, y = nx, ny

print(x,y)    