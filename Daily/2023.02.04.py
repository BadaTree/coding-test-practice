# Q.6096 바둑판(19 * 19)에 흰 돌(1) 또는 검정 돌(0)이 모두 꽉 채워져 놓여있을 때, n개의 좌표를 입력받아 십(+)자 뒤집기한 결과를 출력하는 프로그램을 작성해보자.
# 입력 받은 19*19 바둑판 받아 와서 2차원 배열에 저장하기
list = [[0 for i in range(20)] for j in range(20)]
# 한 줄씩 받아서 입력 받아서 list라는 배열에 저장
for i in range(1,20):
    list[i] = input().split()
    for j in range(1,20):
        list[i][j] = int(list[i][j])
# 뒤집는 횟수 입력 받기
n = int(input())
# 뒤집을 x,y 좌표 입력 받기
change = [[0 for i in range(2)] for j in range(n)]
for i in range(n):
    change[i] = input().split()
    for j in range(2):
        change[i][j] = int(change[i][j])
for i in range(n):
    for j in range(1,20):
        if list[change[i][0]][j] == 0 :
            list[change[i][0]][j] = 1
        else:
            list[change[i][0]][j] = 0
        if list[j][change[i][1]] == 0 :
            list[j][change[i][1]] = 1
        else:
            list[j][change[i][1]] = 0

for i in range(1,20) :
  for j in range(1,20) :
    print(list[i][j], end=' ')    #공백을 두고 한 줄로 출력
  print()



# Q.6097 격자판의 세로(h), 가로(w), 막대의 개수(n), 각 막대의 길이(l), 막대를 놓는 방향(d:가로는 0, 세로는 1)과
# 막대를 놓는 막대의 가장 왼쪽 또는 위쪽의 위치(x, y)가 주어질 때,격자판을 채운 막대의 모양을 출력하는 프로그램을 만들어보자.

# Q.6098 10*10 크기의 미로 상자의 구조와 먹이의 위치가 입력된다. 성실한 개미가 이동한 경로를 9로 표시해 출력한다.