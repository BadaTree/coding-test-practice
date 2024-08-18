#
# # Q.6092 이상한 출석 번호 부르기1
# n = int(input()) #출석 부르는 횟수 입력
# a = input().split() # n번의 부르는 번호 공백으로 입력
#
# # 부른 출석 번호를 int로 다시 재정렬
# for i in range(n):
#   a[i] = int(a[i])
#
# # 0 ~ 23 출석 번호가 불린 횟수를 담는 리스트 선언 각 인덱스는 출석 번호를, 인덱스 안에 값은 불린 횟수를 의미함.
# d = [0 for i in range(24)]
# for i in range(n):
#   d[a[i]] +=1
#
# for i in range(1,24):
#   print(d[i],end=' ')
#
# # Q.6093 이상한 출석 번호 부르기2
# n = int(input()) #출석 부르는 횟수 입력
# a = input().split() # n번의 부르는 번호 공백으로 입력
#
# # 부른 출석 번호를 int로 다시 재정렬
# for i in range(n):
#   a[i] = int(a[i])
#
# for i in range(n-1,-1,-1):
#     print(a[i], end =' ')
#
# # Q.6094 이상한 출석 번호 부르기3
# n = int(input()) #출석 부르는 횟수 입력
# a = input().split() # n번의 부르는 번호 공백으로 입력
# min = 100
# # 부른 출석 번호를 int로 다시 재정렬
# for i in range(n):
#   a[i] = int(a[i])
#   if min > a[i] :
#     min = a[i]
#
# print(min)

# Q.6095 바둑판(19 * 19)에 n개의 흰 돌을 놓는다고 할 때, n개의 흰 돌이 놓인 위치를 출력하는 프로그램을 작성해보자.
n = int(input())
xy = [[0 for col in range(2)] for row in range(n)]

for i in range(n):
    xy[i][0],xy[i][1] = input().split()
    xy[i][0] = int(xy[i][0])
    xy[i][1] = int(xy[i][1])

a = [[0 for col in range(20)] for row in range(20)]

for i in range(n):
    a[xy[i][0]][xy[i][1]] = 1

for i in range(1, 20) :
  for j in range(1, 20) :
    print(a[i][j], end=' ')    #공백을 두고 한 줄로 출력
  print()

