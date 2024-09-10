# n = int(input())
# list = input().split()
# v = int(input())
# count = 0
# for i in range(n):
#     list[i] = int(list[i])
#     if v == list[i]:
#         count += 1
# print(count)

# N, X = input().split()
# N = int(N)
# X = int(X)
# num = input().split()
# final = []
#
# for i in range(N):
#     if int(num[i])< X:
#         final.append(int(num[i]))
# print(*final)

# @@ 10798번 세로 읽기
in_put = [['0' for j in range(int(15))] for i in range(int(5))]
max_len = 0

for i in range(5):
    temp = input()
    if max_len < len(temp):
        max_len = len(temp)
    in_put[i] = [0 for i in range(len(temp))]
    for j in range(len(temp)):
        in_put[i][j] = temp[j]

for j in range(max_len):
    for i in range(in_put):
       if i[j].isnan:
        i[j]
    b = [i[j] for i in in_put]
    print(b)