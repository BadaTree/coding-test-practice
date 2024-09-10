# # # TODO : 간단하게 코드 사용할 때 사용하는 메모장 노트

# # import sys

# input = sys.stdin.read
# data = input().split()

# data = list(map(int,data[1:]))

# data.sort()

# for i in data :
#     print(i)

# [ ] 백준 1427
# N = list(input())

# N.sort(reverse=True)

# print(''.join(N))

# [ ] 백준 2720

# N = int(input())
# moneys = [25,10,5,1]

# for i in range(N) :
#     pay = int(input())
#     result = []
#     for money in moneys :
#         result.append(str(int(pay / money)))
#         pay = pay % money
  
#     print(' '.join(result))


# while True:
#     n,m = input().split(' ')
#     n,m = int(n), int(m)
#     if n == 0 or m == 0:
#         break
#     check = max(n,m) % min(n,m) == 0 
#     if not check :
#         print("neither")
#     elif n < m and check:
#         print("factor")
#     else:
#         print("multiple")

# N,K = map(int,input().split(' '))
# factor = [i for i in range(1,N+1) if N%i == 0]

# print(factor[K-1] if len(factor)>= K else 0)

# while True:
#     N = int(input())
#     if N == -1 :
#         break
#     factor = [i for i in range(1,N) if N%i == 0]
#     if N == sum(factor): # 완전수라면
#         print( f"{N} = " + " + ".join(map(str, factor)))
#     else :
#         print(f"{N} is NOT perfect.")


#[ ] 백준 1979

# N = int(input())
# nums = list(map(int,input().split()))

# print(sum([1 for num in nums if len([i for i in range(2, num) if num % i == 0]) == 0 and num > 1]))


#[ ] 백준 2581
# def is_prime(num):
#     if num <= 1:
#         return False
#     for i in range(2, int(num ** 0.5) + 1):
#         if num % i == 0:
#             return False
#     return True

# N = int(input())
# M = int(input())
# result = [num for num in range(N, M + 1) if is_prime(num)]

# print(f"{sum(result)}\n{min(result)}") if result else print(-1)

# print(4 ** 0.5,sqrt(4))

# x, y, w, h = map(int,input().split(' '))
# point=[(x,0),(0,y),(x,h),(w,y)]

# print(int(min([(((x-i)**2+(y-j)**2)**0.5) for i,j in point])))

# from collections import Counter

# x_list = []
# y_list = []
# for i in range(3):
#     x,y = input().split(" ")

#     x_list.append(x)
#     y_list.append(y)

# x_Count = Counter(x_list)
# y_Count = Counter(y_list)

# print(next(x for x in x_Count if x_Count[x]==1),next(y for y in y_Count if y_Count[y]==1))

# [ ] 백주 9063
# N = int(input())

# max_x = -100000
# min_x = 100000
# max_y = -100000
# min_y = 100000


# for i in range(N):
#     if N == 1:
#         break
    
#     x,y = map(int,input().split(' '))
#     if x > max_x:
#         max_x = x
#     if x < min_x:
#         min_x = x
#     if y > max_y:
#         max_y = y
#     if y < min_y:
#         min_y = y

# print((max_x-min_x)*(max_y-min_y) if N != 1 else 0)

# [ ] 백준 5073

# import sys

# data = sys.stdin.read().split()
# set_tri = set()

# for i in range(0,len(data),3):
#     triangle = [int(data[i]),int(data[i+1]),int(data[i+2])]
  
#     if triangle == [0,0,0]:
#         break
#     else:
#         # 삼각형의 조건을 만족하지 못할 때
#         if max(triangle) >= (sum(triangle)-max(triangle)):
#             print("Invalid")
#         else :
#             set_tri = set(triangle)
#             if len(set_tri) == 1:
#                 print("Equilateral")
#             if len(set_tri) == 2:
#                 print("Isosceles")
#             if len(set_tri) == 3:
#                 print("Scalene")

# import sys

# input_data = sys.stdin.read().strip().splitlines()

# for line in input_data:
#     a, b, c = map(int, line.split())
    
#     if a == 0 and b == 0 and c == 0:
#         break
    
#     sides = [a, b, c]
#     sides.sort()  # 세 변의 길이를 오름차순으로 정렬
    
#     if sides[2] >= sides[0] + sides[1]:
#         print("Invalid")
#     elif a == b == c:
#         print("Equilateral")
#     elif a == b or b == c or c == a:
#         print("Isosceles")
#     else:
#         print("Scalene")

# nums = list(map(int,input().split(' ')))
# nums.sort(reverse = True)

# # 삼각형의 조건을 만족할 때
# if nums[0]< nums[1]+nums[2] :
#     print(sum(nums))
# else :
#     print((nums[1]+nums[2])*2 -1)

# import sys


# a,b,c= map(int,sys.stdin.read().splitlines())

    
# if sum([a,b,c]) != 180 :
#     print("Error")
# elif a == b == c :
#     print("Equilateral")
# elif a==b or b==c or c==a:
#     print("Isosceles")
# else:
#     print("Scalene")
    
# n = int(input())
# print(2 *( n + 2))


# import sys

# N = int(input())

# scores = []
# for i in range(N):
#     score = input()
#     scores.append(int(score))

# scores.sort()
# for i in scores:
#     print(i)

# [ ] 1934 백준
# def compute_lcm(a, b):
#     for j in range(1,45001):  
#         if (max(a,b)*j) % min(a,b) == 0:
#                 print(max(a,b)*j)
#                 break
# import math

# N = int(input())

# for i in range(N):
#     a,b = map(int, input().split(" "))

#     print(math.lcm(a, b))

#[ ] 백준 1735
# import math

# a1, a2 = map(int, input().split())
# b1, b2 = map(int, input().split())

# # 최소공배수(LCM) 구하기
# lcm = math.lcm(a2, b2)

# # 분수를 공통 분모로 변환하여 합 계산
# c1 = a1 * (lcm // a2) + b1 * (lcm // b2)
# c2 = lcm


# gcd = math.gcd(c1, c2)

# # 분자와 분모를 최대공약수로 나누기
# c1 //= gcd
# c2 //= gcd

# # 결과 출력
# print(f"{c1} {c2}")

# [ ] 11650 좌표 정렬하기
# import sys

# N = int(input())
# points =[]
# input = sys.stdin.read().splitlines()
# for point in input:
#     x,y = point.split()
#     points.append([int(x), int(y)])

# points.sort()
# for i in range(N):
#     print(points[i][0],points[i][1])
    
    
# [ ] 11651 좌표 정렬하기 2

# N = int(input())
# points =[]

# for point in range(N):
#     x,y = input().split()
#     points.append([int(y),int(x)])

# points.sort()
# for i in range(N):
#     print(points[i][1],points[i][0])

# [ ] 10814 나이순 정렬
# import time

# start = time.time()
# N = int(input())
# members = []

# for i in range(N):
#     age,name = input().split()
#     members.append([int(age), i,name])
    
# members.sort(key=lambda x :(x[0],x[1]))

# for i in range(N):
#     print(members[i][0],members[i][2])
# end = time.time()

# print(end-start)


#[ ] 28278 스택 2

'''
N = int(input())

stack_list = []
for i in range(N):
    result = 0
    command = list(map(int,input().split(' ')))
    if command[0] == 1:
        stack_list.append(command[1])
    else:
        if command[0] == 2 :
            if stack_list:
                result = stack_list.pop()
            else:
                result = -1
        elif command[0] == 3 :
            result = len(stack_list)
        elif command[0] == 4 :
            result = 0 if stack_list else 1
        elif command[0] == 5:
            if stack_list:
                result = stack_list[-1]
            else:
                result = -1
        print(result)

# NOTE : 위 코드 시간 초과 -> sys.stdin으로 한 번에 읽기, 
# 결과 result 리스트에 저장하고 한번에 출력하기

import sys
input = sys.stdin.read

N, *commands = input().split()

N = int(N)
commands = list(map(int, commands))

stack_list = []
result = []

i = 0
while i < len(commands):
    command = commands[i]
    if command == 1:
        stack_list.append(commands[i + 1])
        i += 2
    elif command == 2:
        if stack_list:
            result.append(stack_list.pop())
        else:
            result.append(-1)
        i += 1
    elif command == 3:
        result.append(len(stack_list))
        i += 1
    elif command == 4:
        result.append(0 if stack_list else 1)
        i += 1
    elif command == 5:
        if stack_list:
            result.append(stack_list[-1])
        else:
            result.append(-1)
        i += 1

sys.stdout.write('\n'.join(map(str, result)) + '\n')
'''

# [ ] 10773 
'''

N = int(input())
nums =[]

for i in range(N):
    num = int(input())
    if not num:
        nums.pop()
    else:
        nums.append(num)
print(sum(nums))
'''

# [ ] 18258 큐 2 
'''
import sys 
from collections import deque

queue = deque()
result = []
input = sys.stdin.readlines()
N = int(input[0].strip())

for i in range(1,N+1):
    command = input[i].strip().split()

    if command[0] == "push":
        queue.append(int(command[1]))
    elif command[0] == "push":
        result.append(queue.popleft() if queue else -1)
    elif command[0] == "size":
        result.append(len(queue))
    elif command[0] == "empty":
        result.append(0 if queue else 1)
    elif command[0] == "front":
        result.append(queue[0] if queue else -1)
    elif command[0] == "back":
        result.append(queue[-1] if queue else -1)

print('\n'.join(map(str,result)))

'''

# [ ] 11866 
'''
N,K = map(int,input().split(' '))

nums = [True]* (N)
p = -1 # 이동 위치를 저장()
m = 0 
result = []

# 모든 사람이 제거될 때까지 반복
while(sum(nums) != 0):
    # 0번 째부터 포인터 이동하면서 K 번 째 사람 찾기
    p += 1
    if p == N: # 마지막 인덱스에서 첫 인덱스로 넘어갈 때 (원형구조 구현)
        p = 0

    if nums[p]: # 살아있는 사람만 카운트. 죽은 사람은 그냥 패스  
        m += 1
    # K번 째 제거 대상을 찾았을 때 !
    if m == K: 
        result.append(p+1)
        nums[p] = False
        m = 0
        
print(f"<{', '.join(map(str,result))}>")

from collections import deque

N,K = map(int,input().split(' '))
result = []

queue = deque([i for i in range(1,N+1)])

while queue:
    queue.rotate(-(K-1))
    result.append(queue.popleft())
    
print(f"<{', '.join(map(str,result))}>")
'''

#[ ] 28279 덱 2
'''
import sys
from collections import deque

input = sys.stdin.read().splitlines()
N = int(input[0])
queue = deque()
result = []

for i in range(1,N+1):
    command = input[i].split(' ')
    if command[0] == '1':
        queue.appendleft(command[1])
    elif command[0] == '2':
        queue.append(command[1])
    elif command[0] == '3':
        result.append(queue.popleft() if queue else -1)
    elif command[0] == '4':
        result.append(queue.pop() if queue else -1)
    elif command[0] == '5':
        result.append(len(queue))
    elif command[0] == '6':
        result.append(0 if queue else 1)
    elif command[0] == '7':
        result.append(queue[0] if queue else -1)
    elif command[0] == '8':
        result.append(queue[-1] if queue else -1) 

print('\n'.join(map(str,result))) 
'''

# [ ] 백준 2346         
'''
from collections import deque

N = int(input())
move = list(map(int, input().split(' ')))
result = []

queue = deque([i for i in range(1,N+1)])
# 1번 풍선 터트리기. 터진 풍선 인덱스 저장 
result.append(queue.popleft())

for i in range(N-1):
    # move[result[i]]통해 터진 풍선 속 종이 값 찾고, 그만큼 이동한다
    m = result[i] - 1
    if move[m] > 0:
        queue.rotate(-(move[m]-1))
        # 이동한 위치 풍선 터뜨리기
        result.append(queue.popleft())
    else :
        queue.rotate(-(move[m]+1))
        # 이동한 위치 풍선 터뜨리기
        result.append(queue.pop())
    
print(' '.join(map(str,result)))
'''

# [ ] 백준 15439
'''
N = int(input())
#상의 1개당 고를 수 있는 하의는 N-1개 즉 총 조합은 N*(N-1)
print(N*(N-1))
'''

# [ ] 백준 24723
'''
N = int(input())
#상의 1개당 고를 수 있는 하의는 N-1개 즉 총 조합은 N*(N-1)
print(2**N)
'''

# [ ] 백준 10872 
'''
N = int(input())
result = 1

for i in range(1,N+1):
    result *= i
print(result)
'''

#[ ] 백준 11050 
# NOTE: 이항계수가 뭐지?

'''
def factorial(n):
    result = 1
    for i in range(1,n+1):
        result *= i
    return result

N,K = map(int,input().split(' '))

print(factorial(N) // (factorial(K) * factorial(N - K)))
'''

# [ ] 백준 1010
# NOTE: M>N일 때, M개 중에 N개를 고르는 경우의 수에서 왜 이항계수를 활용..?
'''
def factorial(n):
    result = 1
    for i in range(1,n+1):
        result *= i
    return result

T = int(input())
for i in range(T):
    N,M = map(int,input().split(' '))

    print(factorial(M) // (factorial(N) * factorial(M - N)))
'''

# [ ] 백준 1037
'''
N = int(input())

nums = list(map(int,input().split(' ')))

nums.sort()

print(nums[0]*nums[-1])
'''

# [ ] 백준 25192
'''
import sys

input = sys.stdin.read().strip().splitlines()
N = int(input[0])
records = input[1:]

greeted_users = set()
count = 0

for msg in records:
    if msg == "ENTER":
        greeted_users.clear()
    else:
        if msg not in greeted_users:
            greeted_users.add(msg)
            count += 1

print(count)

'''

# [ ] 백준 26069
'''
N = int(input())

# 춤을 추는 사람들을 저장하는 집합
dance = set()
dance.add('ChongChong')

for _ in range(N):
    a, b = input().split()
    
    if a in dance or b in dance:
        dance.add(a)
        dance.add(b)

print(len(dance))
'''

# [ ] 백준 2108 
'''
import sys
from collections import Counter as CollectionsCounter

def custom_counter(num):
    nums_count = CollectionsCounter(num)
    max_count = max(nums_count.values())
    mode = [ key for key,value in nums_count.items() if value == max_count]
    mode.sort()
   
    return mode[0] if len(mode)==1 else mode[1]

input_data = sys.stdin.read().splitlines()

N = int(input_data[0])

nums = list(map(int, input_data[1:]))
nums.sort()

print(round(sum(nums) / N))  # Mean
print(nums[(N-1)//2] if N != 1 else nums[0])  # Median
print(custom_counter(nums))  # Mode count
print(nums[-1]-nums[0])  # Range
'''

# [ ] 백준 20920 
# NOTE : 빈도수, 길이는 내림차순, 사전순은 오름차순으로 정렬해야함.
'''
# N,M 받기 
# M 미만 단어 필터링
# 자주 나오는 단어일수록 앞에 배치한다.
# 같은 빈도수 있는 단어는 단어의 길이가 길수록 앞에 배치한다.
# 길이가 같은 단어들은 알파벳 사전 순으로 앞에 있는 단어일수록 앞에 배치한다

N,M = map(int,input().split(' '))
words = []
set_w = set()
result = []
sorted_r =[]

# 1. 단어 받기 & M 미만 단어 필터링
for i in range(N):
    word = input()
    # M 미만 단어 필터링
    if len(word)>= M:
        words.append(word)

# 2. 단어 빈도수, 단어 길이 기준으로 내림차순 정렬
set_w = set(words)

for w in set_w:
    # [ 단어 빈도수, 단어 길이, 단어 ] 로 결과 배열 저장 
    result.append([words.count(w),len(w),w])
    
result.sort(reverse=True)

# 3. 단어 길이 같은 애들은 알파벳 오름차순으로 정렬
sorted_r = [(10-result[i][1],result[i][2])for i in range(len(result))]


print('\n'.join([i[1] for i in sorted_r ]))

import sys
from collections import Counter

# 입력 받기
input = sys.stdin.read
data = input().split()

N = int(data[0])
M = int(data[1])
words = data[2:]

# M 미만 단어 필터링 및 단어 빈도수 계산
filtered_words = [word for word in words if len(word) >= M]
word_count = Counter(filtered_words)

# 정렬 기준에 따라 단어 정렬
# Counter({'banana': 3, 'apple': 2, 'cherry': 1})로 x(key,value) 즉 x[0]:단어,x[1]:빈도수 
sorted_words = sorted(word_count.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))

# 출력
for word, _ in sorted_words:
    print(word)
'''

# [ ] 백준 25206
# 학점 등금 
'''
import sys

data = sys.stdin.read().strip().splitlines()
scores = {'A+' : 4.5, 'A0': 4.0, 'B+':3.5, 'B0':3.0, "C+":2.5, 'C0': 2.0,'D+':1.5,'D0':1.0,'F':0.0}
score_avg = 0
score_sum = 0
gpa = 0 

for i in range(20):
    score = data[i].split(' ')
    if score[2] != 'P':
        score_sum += float(score[1])
        score_avg += float(score[1])*float(scores[score[2]])
        
gpa = score_avg / score_sum if score_sum > 0 else 0.0

print("{:.6f}".format(gpa))

'''
# [ ] 백준 2798 
'''
N,M = map(int, input().split(' '))
jack = 100000
nums = list(map(int,input().split(' ')))
nums.sort(reverse=True)
find = 0

def find_jack(i,nums):
    result = 0 
    for j in range(i+1,len(nums)):
        if M>=sum([nums[i],nums[j]]) :
            for k in range(i+j+2,len(nums)):
                if M>=sum([nums[i],nums[j],nums[k]]) :
                    result = sum([nums[i],nums[j],nums[k]])
                    break
    
    return result

# M에 최대한 가까운 카드 3장의 합을 찾을 때까지 반복
# 첫번쨰 카드 고르기

for i in range(len(nums)-2):
    if jack <= M:
        break
    else:
        if sum([nums[i],nums[i+1]]) < M:
            jack = find_jack(i,nums)
            
print(jack)


from itertools import combinations

def blackjack(N, M, cards):
    max_sum = 0
    # 가능한 3장의 카드 조합을 생성.
    for combo in combinations(cards, 3):
        current_sum = sum(combo)
        # 합이 M을 넘지 않으면서 최대값을 갱신합니다.
        if max_sum < current_sum <= M:
            max_sum = current_sum
    return max_sum

# 입력 처리
N, M = map(int, input().split())
cards = list(map(int, input().split()))
print(list(combinations(cards, 3)))
# 결과 출력
print(blackjack(N, M, cards))

from itertools import combinations


def find_jack(N,M,nums):
    max_sum = 0
    # 카드 중에서 세 가지를 뽑는 조합 생성
    for comb in combinations(nums,3):
        current_sum = sum(comb)
        # 그 합이 M을 넘지 않으면서 가장 큰 값 갱신하며 찾기
        if max_sum < current_sum <= M:
            max_sum = current_sum
    return max_sum

N,M = map(int, input().split(' '))
nums = list(map(int,input().split(' ')))

print(find_jack(N,M,nums))

'''

# [ ] 백준 2231
'''
from itertools import product

def find_M(N,nums):
    min_M = 100000000

    for m in list(product(nums,repeat=len(str(N)))):
        M = int(''.join(map(str,m)))
    
        if (sum(m) + M) == N and M < min_M:
            min_M = M
    return min_M if min_M != 100000000 else 0

N = int(input())
nums = [i for i in range(0,10)]

print(find_M(N,nums))

def find_smallest_constructor(target):
    # 각 자리수의 합이 최대 9이므로 탐색 시작점을 target - 9 * len(str(target))로 설정
    start = max(1, target - 9 * len(str(target)))
    
    for candidate in range(start, target):
        sum_with_digits = candidate + sum(map(int, str(candidate)))
        if sum_with_digits == target:
            return candidate
    return 0

# 입력 처리
target = int(input())

# 결과 출력
print(find_smallest_constructor(target))
'''

# [ ] 백준 19532
'''
# 해가 하나이고, 변수와 방정식의 수가 동일한 연립 방정식 풀기 -> 크래머 공식
# 크래머 공식으로 풀기

a,b,c,d,e,f =map(int,input().split(' '))

A = a*e - b*d
A1 = c*e - b*f
A2 = a*f - c*d
print(A1//A, A2//A)
'''

# [ ]
'''
a,b,c = map(int,input().split(' '))
print(a+b+c)
'''
'''
print("\\    /\\")
print(" )  ( ')")
print("(  /  )")
print(" \(__)|")
'''
'''
print("|\_/|")
print("|q p|   /}")
print("( 0 )\"\"\"\\")
print("""|"^"`   |""")
print("||_/=\\__|")

'''

'''
N= int(input())
for i in range(1,10):
    print(f"{N} * {i} = {N*i}")
'''
'''
N = int(input())
print(sum([i for i in range(1,N+1)]))
'''
'''
total_price = int(input())
N = int(input())

final_price = 0

for i in range(N):
    price,n = map(int,input().split(" "))
    final_price += price*n

print("Yes" if total_price == final_price else "No")
'''
'''
N = int(input())

print(("long"+" ")*(N//4)+"int")
'''
'''
import sys

input = sys.stdin.read().strip().splitlines()

N = int(input[0])


for i in range(1,N+1):
    a,b = map(int,input[i].split(' '))
    print(a+b)
    '''
'''
N = int(input())

[print(' ' * (N-i)+'*' * i) for i in range(1, N + 1)]
'''
'''
import sys

input = sys.stdin.read().splitlines()
running =  True 
i = 0

[print(int(input[i][0])+ int(input[i][2])) for i in range(len(input)) ]
'''
'''
import sys

nums = sys.stdin.read().splitlines()
nums = list(map(int, nums))

print(max(nums))
print(nums.index(max(nums))+1)
'''

# [ ] 백준 1002
# 류재명의 위치는 하나임으로 조규현,백승환 둘에 모두 속해야됨.
# 조규현,백승환의 계산한 좌표의 교집합이 류재명이 있을 수 있는 좌표임.

# 입력된 두 점 사이의 거리에 속하는 좌표 반환하는 함수 
import math

def find_point(x,y,xt,yt,r):
    R = math.sqrt((xt-x)**2+(yt-y)**2)
    if R == r :
        return True 
    else :
        return False
    
T = int(input()) 
x1,y1,r1,x2,y2,r2 = map(int,input().split(' '))
x1_set = set()
x2_set = set()

# 조규현 - 류재명 거리로 찾은 예산 위치 
for i in range(-10000,10001):
    for j in range(-10000,10001):
        if find_point(x1,y1,i,j,r1):
            x1_set.add((i,j))
    

# 백승환 - 류재명 거리로 찾은 예산 위치
for i in range(-10000,10001):
    for j in range(-10000,10001):
        if find_point(x2,y2,i,j,r2):
            x2_set.add((i,j))

# 두 Set의 교집합 즉 류재명 가능 위치 수 출력
print(len(x1_set&x2_set))