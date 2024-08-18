# TODO : 0717 백준 풀이

# [ ] 백준 2559 수열 

import sys

data = sys.stdin.read().strip().splitlines()
N,K = map(int,data[0].split(' '))
nums = list(map(int,data[1].split(' ')))
max_sum = 0

for t in range(N):
    temp = sum(nums[t:t+K])
    if max_sum < temp :
        max_sum = temp
print(max_sum)

import sys

# 입력을 받습니다.
data = sys.stdin.read().strip().split()
N = int(data[0])
K = int(data[1])
nums = list(map(int, data[2:]))

current_sum = sum(nums[:K])
max_sum = current_sum

for i in range(K, N):
    current_sum += nums[i] - nums[i - K]
    if current_sum > max_sum:
        max_sum = current_sum

print(max_sum)
