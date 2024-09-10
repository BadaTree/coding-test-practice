# TODO: 4837. [파이썬 S/W 문제해결 기본] 2일차 - 부분집합의 합

case_N = int(input())
arr = []

for i in range(1,13):
    arr.append(i)
    
for c in range(case_N):
    count = 0
    N,K = list(map(int,input().split(' ')))
    for i in range(1<<12):
        temp = []
        for j in range(12):
            if i &(1<<j):
                temp.append(arr[j])
        if len(temp) == N and sum(temp) == K :
            count += 1
    print(f"#{c + 1} {count}")
    