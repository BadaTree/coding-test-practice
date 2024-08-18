# Q.6073 정수(1 ~ 100) 1개가 입력되었을 때 카운트다운을 출력해보자.
num = int(input())
for i in range(1,num+1):
    print(num-(i))

# Q.6074 영문 소문자(a ~ z) 1개가 입력되었을 때, a부터 그 문자까지의 알파벳을 순서대로 출력해보자.
c = ord(input())
t = ord('a')
while t<=c :
  print(chr(t), end=' ')
  t += 1

# Q.6075 정수(0 ~ 100) 1개를 입력받아 0부터 그 수까지 순서대로 출력해보자.
num = int(input())
for i in range(num+1):
    print(i)

# Q.6076 정수(0 ~ 100) 1개를 입력받아 0부터 그 수까지 순서대로 출력해보자.
num = int(input())
for i in range(num+1):
    print(i)

# Q.6077 정수(1 ~ 100) 1개를 입력받아 1부터 그 수까지 짝수의 합을 구해보자.
num = int(input())
sum = 0
for i in range(num+1):
    if i % 2 == 0:
        sum += i
print(sum)

# Q.6078 영문 소문자 'q'가 입력될 때까지 입력한 문자를 계속 출력하는 프로그램을 작성해보자.
while True:
    a = input()
    if a == "q":
        print(a)
        break
    else:print(a)

# Q.6079 1, 2, 3 ... 을 계속 더해 나갈 때,그 합이 입력한 정수(0 ~ 1000)보다 같거나 작을 때까지만 계속 더하는 프로그램을 작성해보자
max_num = int(input())
sum = 0
i = 0
while sum < max_num :
    sum += i
    i += 1
    if sum >= max_num:
        i -= 1
        sum -= i
        break
print(i)

# Q.6080 1부터 n까지, 1부터 m까지 숫자가 적힌 서로 다른 주사위 2개를 던졌을 때, 나올 수 있는 모든 경우를 출력해보자.
n,m = input().split()
n = int(n)
m = int(m)

for i in range(1,n+1):
    for j in range(1,m+1):
        print(i,j)