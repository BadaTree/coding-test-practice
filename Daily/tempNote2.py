# [ ] 백준 1002 
'''
import math

def isPossible(x,y,xt,yt,r):
    R = math.sqrt((xt-x)**2+(yt-y)**2)
    return R == r 

def find_poits(x,y,r):
    result = set()
    
    for i in range(x-r,x+r+1):
        for j in range(y-r,y+r+1):
            if isPossible(x,y,i,j,r):
                result.add((i,j))
    return result
# 교집합 원소를 찾으면 되니까 조규현의 가능 좌표들만 체크 
def find_poits2(x,y,r,points):
    result = set()
    
    for px,py in points:
        if isPossible(x,y,px,py,r):
                result.add((px,py))
            
    return result

x1_set = set()
x2_set = set()

T = int(input()) 

for i in range(T):
    x1,y1,r1,x2,y2,r2 = map(int,input().split())

    # 조규현 - 류재명 거리로 찾은 예산 위치 
    x1_set = find_poits(x1,y1,r1)
        
    # 백승환 - 류재명 거리로 찾은 예산 위치
    x2_set = find_poits2(x2,y2,r2,x1_set)

    # 두 Set의 교집합 즉 류재명 가능 위치 수 출력
    print(len(x2_set))

import math

def find_intersection_count(x1, y1, r1, x2, y2, r2):
    # 두 원의 중심 사이의 거리
    d = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    
    # 동일한 중심
    if d == 0:
        if r1 == r2:
            return -1  # 무한히 많은 교점
        else:
            return 0  # 교점 없음
    
    # 두 원이 서로 만나지 않는 경우
    if d > r1 + r2 or d < abs(r1 - r2):
        return 0  # 교점 없음
    
    # 외접하거나 내접하는 경우
    if d == r1 + r2 or d == abs(r1 - r2):
        return 1  # 한 개의 교점
    
    # 그 외의 경우 (두 개의 교점)
    return 2

# 입력 처리
T = int(input())
results = []
for _ in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    results.append(find_intersection_count(x1, y1, r1, x2, y2, r2))

# 결과 출력
for result in results:
    print(result)
'''

    
# [ ] 백준 5597
'''
import sys

students = sys.stdin.read().splitlines()

set_stud = set(list(map(int,students)))
set_nums = set([i for i in range(1,31)])

# 제출하지 않은 학생의 출석번호 구하기
result = list(set_nums - set_stud)

# 오름차순으로 정렬
result.sort()

[print(n) for n in result]
'''
'''
N,M = map(int,input().split(' '))

print((N-1) + N*(M-1))

'''

# [ ] 백준 3052
'''
import sys

nums = sys.stdin.read().splitlines()
result = set()

for num in nums:
    result.add(int(num)%42)
    
print(len(result))

'''

# [ ] 백준 1546
'''
N = int(input())

scores = map(int,input().split(' '))
best = max(scores)

NewScores = [ score / best*100 for score in scores]

print(round(sum(NewScores)/len(NewScores),6))
'''

# [ ] 백준 27433

'''
N = int(input())
answer = 1

for n in range(1,N+1):
    answer *= n

print(answer)
'''
'''
N = int(input())
result = [0,1]

def fibo(i):
    result.append(result[i-1] + result[i-2])
i = 2

while i <= N:
    fibo(i)
    i += 1
    
print(result[N])
'''

# [ ] 백준 1003 
'''
# 내가 푼 1차 풀이 -> 시간초과 ㅜ
import sys


def fibonacci(n): 
    if n == 0 :
        global zero
        zero += 1
        return 0 
    elif n == 1:
        global one 
        one += 1
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

input = sys.stdin.read().splitlines()
T = int(input[0])
 
for i in range(T):
    zero = 0
    one = 0
    N = int(input[i+1])
    fibonacci(N)
    print(zero, one)
    
'''
'''
import sys

def fibonacci_count(max_N):
    zero_count = [0] * (max_N+1)
    one_count = [0] * (max_N+1)

    zero_count[0], zero_count[1] = 1,0
    one_count[0], one_count[1] = 0,1

    for i in range(2,max_N+1):
        zero_count[i] = zero_count[i-1] + zero_count[i-2] 
        one_count[i] = one_count[i-1] + one_count[i-2] 
        
    return zero_count, one_count

def main():
    input = sys.stdin.read().splitlines()

    T = int(input[0])
    result_case = [int(input[i+1]) for i in range(T)]

    max_N = 40

    zero_count , one_count = fibonacci_count(max_N)


    for i in result_case:
        print(zero_count[i],one_count[i])
        

if __name__ == "__main__":
    main()
'''

# [ ] 백준 24263
'''
n = int(input())

print(n) # code1 수행횟수는 항상 n회
print(1) # 다항식으로 나타내면 n이므로 1

'''

# [ ] 백준 24264 

# n = int(input())

# print(n**2) # code1 수행횟수는 항상 n회
# print(2) # 다항식으로 나타내면 n이므로 1

# # [ ] 백준 24265
# # 1+ 2+ 3+ ...+ n-1 = n(n-1)/2

# n = int(input())

# # 코드1의 수행 횟수는 (n * (n - 1)) // 2
# if n == 1:
#     print(0)
# else:
#     print((n * (n - 1)) // 2)

# # 최고차항의 차수는 항상 2
# print(2)

# # [ ] 백준 24266

# n = int(input())

# print(n**3)

# # 최고차항의 차수는 항상 2
# print(3)


# [ ] 백준 24267
'''
n = int(input())

# 코드1의 수행 횟수는 (n * (n - 1) * (n - 2)) // 6
if n < 3:
    print(0)
else:
    print((n * (n - 1) * (n - 2)) // 6)

# 최고차항의 차수는 항상 3
print(3)
'''

# [ ] 백준 24313 
'''
a1,a0 = map(int,input().split(' '))
C= int(input())
n = int(input())

print(1 if (a1*n + a0) <= C*n and a1 <= C else 0)

'''

# [ ] Programers 최대공약수 최소 공배수 
'''
# 유클리드호제법을 활용한 최대공약수 구하기
def GCD(a,b):
    while b != 0:
        a,b = b, a%b 
    return a 
# 최소 공배수 구하기
def lcm(a,b):
    return a*b // GCD(a,b)

print(GCD(36,20),lcm(36,20))
'''
'''
word = input()
n = int(input())

print(word[n-1])
'''
'''
N = int(input())

for i in range(N):
    word = input()
    print(f"{word[0]}{word[-1]}")
'''
'''
print(len(input().strip().split(' ')))
'''
'''
import sys

inputData = sys.stdin.read().splitlines()

for i in inputData:
    print(i)
'''
'''
import sys

input = sys.stdin.read().splitlines()
T = int(input[0])

for i in range(1,len(input)):
    n,w = input[i].split(' ')
    n = int(n)
    print(''.join([i*n for i in w]))

'''

#  [ ] 백준 구간합 구하기4
# i번째 수부터 j번째 수까지 합 구하는 방법
# 1. sum(nums[i-1:j]) 해서 하나씩 계산 : 총 시간 복잡도는 O(M * N) -> 시간 초과
# 2. 누적합 배열을 활용해서 각 인덱스까지의 누적합을 저장하는 배열 생성, 
# prefix_sum[j]-prefix_sum[i-1] 하여 연산 : O(1) -> 훨씬 효율적임 !

'''
import sys

input = sys.stdin.read().splitlines()

N,M = map(int,input[0].split(' '))
nums = list(map(int,input[1].split(' ')))


# 누적합 배열 만들기 
prefix_sum = [0]*(N+1)

# 누적합 구하기 
for n in range(1,N+1):
    prefix_sum[n] = prefix_sum[n-1] + nums[n-1]


for m in range(2,M+2):
    i,j = map(int, input[m].split(' '))
    print(prefix_sum[j]-prefix_sum[i-1])

'''

# [ ] 백준 2559 수열 
'''
import sys

input = sys.stdin.read().splitlines()

N,K = map(int,input[0].split(' '))
temp = list(map(int,input[1].split(' ')))


# 누적합 배열 만들기 
prefix_sum = [0]*(N)

# 누적합 구하기 
for n in range(N):
    prefix_sum[n] = sum(temp[n:n+K])

print(max(prefix_sum))

'''

# [ ] 백준 1157

'''
from collections import Counter

word = input().lower() # 대소문자를 구분하지 않으므로 소문자로 통일 시켜줌

count_word = dict(Counter(word))
max_alpha = max(count_word.values())

# 최대 빈도 가지는 알파벳의 수 세기
max_count = sum([1 for value in count_word.values() if max_alpha == value])

# 최대 빈도 가지는 알파벳의 수가 1개라면 대문자 알파벳 출력, 여러개라면 ? 출력

if max_count > 1:
    print("?")
else :
    for alpha,value in count_word.items():
        if value == max_alpha:
            print(alpha.upper())
            break
'''

# [ ] 백준 9655


# [ ] 백준 10813

N,M = map(int,input().split(' '))

baskets = [i for i in range(N + 1)]

# 공 교환
for _ in range(M):
    i, j = map(int, input().split())
    baskets[i], baskets[j] = baskets[j], baskets[i]

# 결과 출력 (1번 바구니부터 N번 바구니까지)
print(' '.join(map(str, baskets[1:])))
    



