N,M,K = map(int, input().split()) 
data = []
k = 0
sum = 0

for _ in range(N):
    data.append(int(input()))
data.sort(reverse=True)

for _ in range(0,M):
    if not(k > K):
        sum += data[0]
        k += 1
    else:
        k = 0
        sum += data[1]
print(sum)
         
            
# NOTE: 큰 수와 두 번째 큰 수의 더해지는 횟수를 계산하여 구현하는 법칙
N,M,K = map(int, input().split()) 
data = []
k = 0
sum = 0

for _ in range(N):
    data.append(int(input()))

# 내림차순으로 정렬    
data.sort(reverse=True)

# 큰 수가 더해지는 횟수 계산
Count = int(M/(K+1) * K)
Count += M %( K+1)

total_sum = Count * data[0]
total_sum += (M-Count)*data[1]

print(total_sum)
