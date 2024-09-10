# Q.6081 A, B, C, D, E, F 중 하나가 입력될 때, 1부터 F까지 곱한 16진수 구구단의 내용을 출력해보자.
num16 = int(input())
for i in range(1,16):
    result = num16 * i
    print('%X' % num16, '*%X' % i, '=%X' % (result), sep='')
# Q.6082 친구들과 함께 3 6 9 게임을 하던 영일이는 잦은 실수 때문에 계속해서 벌칙을 받게 되었다.
# 3 6 9 게임의 왕이 되기 위한 369 마스터 프로그램을 작성해 보자.
num = int(input())
for i in range(1,num+1):
    if i % 10 == 3 or i % 10 == 6 or i % 10 == 9:
        print("X", end=' ')
    else: print(i, end=' ' )

# Q.6083 빨강(red), 초록(green), 파랑(blue) 빛을 섞어 여러 가지 다른 색 빛을 만들어 내려고 한다.
#  빨강(r), 초록(g), 파랑(b) 각 빛의 가짓수가 주어질 때,주어진 rgb 빛들을 섞어 만들 수 있는 모든 경우의 조합(r g b)과 만들 수 있는 색의 가짓 수를 계산해보자.
R,G,B = input().split()
count= 0
for i in range(int(R)):
    for j in range(int(G)):
        for k in range(int(B)):
            print(i,j,k)
            count += 1
print(count)
# Q.6084 소리 파일 저장 용량 계산하기
h,b,c,s = input().split()
result = int(h)*int(b)*int(c)*int(s)
print(round(result/8/1024/1024,1),"MB")

# Q.6085 그림 파일 저장용량 계산하기
w,h,b = input().split()
result = int(w)*int(h)*int(b)
print(round(result/8/1024/1024,2),"MB")

# Q.6086 1, 2, 3 ... 을 순서대로 계속 더해 합을 만드는데, 그 합이 입력한 정수보다 작을 동안만 계속 더하는 프로그램을 작성해보자.
num = int(input())
sum = 0
i = 1
while sum < num:
    sum += i
    i += 1
print(sum)

# Q.6087 1부터 입력한 정수까지 1씩 증가시켜 출력하는 프로그램을 작성하되, 3의 배수인 경우는 출력하지 않도록 만들어보자.
num = int(input())
for i in range(1,num+1):
    if i % 3 != 0 :
        print(i,end='')

# Q.6088 시작 값(a), 등차(d), 몇 번째인지를 나타내는 정수(n)가 입력될 때, n번째 수를 출력하는 프로그램을 만들어보자.
a,d,n = input().split()
a = int(a)
d = int(d)
n = int(n)
result = a + ((n-1)*d)
print(result)

# Q.6089 시작 값(a), 등비(r), 몇 번째인지를 나타내는 정수(n)가 입력될 때, n번째 수를 출력하는 프로그램을 만들어보자.
a,d,n = input().split()
a = int(a)
d = int(d)
n = int(n)
result = a * ((n-1)**d)
print(result)
# Q.6090 시작 값(a), 곱할 값(m), 더할 값(d), 몇 번째인지를 나타내는 정수(n)가 입력될 때, n번째 수를 출력하는 프로그램을 만들어보자.
a, m, d, n = input().split()
a = int(a)
d = int(d)
n = int(n)
m = int(m)

i = 1
before = a

while i < n:
    before = (before * m) + d
    i += 1

print(before)

# Q.6091 3명이 다시 모두 함께 방문해 문제를 풀어보는 날(동시 가입/등업 후 며칠 후?)을 출력한다.
a,b,c = input().split()
a = int(a)
b = int(b)
c = int(c)
day = 1

while day % a != 0 or day % b != 0 or day % c != 0:
    day += 1
print(day)