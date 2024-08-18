# a,b = input().split()
# print(int(a)*int(b))

# a,b = input().split()
# print(int(a)+int(b))
# print(int(a)-int(b))
# print(int(a)*int(b))
# print(int(a)//int(b))
# print(int(a)%int(b))
#
# chess = input().split()
# if int(chess[0]) != 1:
#    chess[0] = 1 - int(chess[0])
# else:
#     chess[0] = 0
# if int(chess[1]) != 1:
#    chess[1] = 1 - int(chess[1])
# else:
#     chess[1] = 0
# if int(chess[2]) != 2:
#    chess[2] = 2 - int(chess[2])
# else:
#     chess[2] = 0
# if int(chess[3]) != 2:
#    chess[3] = 2 - int(chess[3])
# else:
#     chess[3] = 0
# if int(chess[4]) != 2:
#    chess[4] = 2 - int(chess[4])
# else:
#     chess[4] = 0
# if int(chess[5]) != 8:
#    chess[5] = 8 - int(chess[5])
# else:
#     chess[5] = 0
# print(chess[0],chess[1],chess[2],chess[3],chess[4],chess[5])

N = int(input())

for i in range(N):
    print(' '*(N-i)+'*'*(i*2-1))
for i in range(N-1,-1,-1):
    print(' '*(N-i) +'*' * (i * 2 -1))