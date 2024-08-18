# # TODO: 부루트 포스, 완전 탐색을 공부해보자

# # [ ] 프로그래머스 소수 찾기 
# # https://school.programmers.co.kr/learn/courses/30/lessons/12921

# # 1차 시도 10,11,12에서 시간 초과가 뜨고, 효율성도 시간초과... ㅋㅋ
# # '에라토스테네네스의 체' 풀이로 풀어보기 도전..!

# # NOTE: 왜 제곱근까지만 봐도 되는지, 에라토스테네스의 체가 뭔지 공부 
# # 1,자기 자신을 제외한 약수가 발견되면 answer +1 , break 
# import math
# def is_prime(i):
#     result = 1
#     for j in range(2,math.sqrt(i)): # n의 약수 중 하나는 무조건 제곱근 이하이므로 제곱근까만 검사 
#             if i % j == 0 :
#                 result = 0
#                 break
#     return result


# def solution(n):
#     result = 0
#     # 2 부터 n까지 소수인지 체크 %1은 소수가 아님
#     for i in range(2,n+1):
#         result += is_prime(i)
#     return result

# '에라토스테네스의 체'를 활용한 풀이 

def solution(n):
    num=set(range(2,n+1))

    for i in range(2,n+1):
        if i in num:
            num-=set(range(2*i,n+1,i))
    return len(num)


def solution(n):
    nums = [i for i in range(2,n+1)]
    
    for i in range(len(nums)):
        if nums[i] == 0 :
            pass
        else:
           for j in range(i+1,n+1):
                if nums[j] % nums[i] == 0 :
                    nums[j] == 0 
    for i in nums :
        if i != 0 :
            print(i)
n = 10
                
nums = [1 for i in range(n+1)]
nums[0],nums[1] =0,0

for i in range(2,n):
    if nums[i] == 0 :
        pass
    else:
        for j in range(i+1,n+1):
            if j % i == 0 and nums[j] != 0:
                nums[j] = 0 
          
print(sum(nums))
for i in range(len(nums)) :
    if nums[i] != 0 :
        print(i)
    
# [ ] 

from itertools import permutations
import math

def is_prime(n):
    # 0이나 1은 소수가 아님
    if n == 0 or n == 1:
        return False
    else:# 1과 자신 이외의 약수가 있어도 소수가 아님
        for i in range(2,int(math.sqrt(n))+1):
            if n % i == 0 :
                return False
    return True

def solution(numbers):
    set_nums = set()
    result = 0
    
    # 종이로 만들 수 있는 수 조합 
    for i in range(1,len(numbers)+1):
        for p in permutations(numbers,i):
            tmp = int(''.join(p))
            set_nums.add(tmp)
    # 조합 중에 소수가 몇 개인지 판별 
    for i in set_nums:
        result += int(is_prime(i))
        
    return result


from itertools import permutations
def solution(n):
    a = set()
    for i in range(len(n)):
        a |= set(map(int, map("".join, permutations(list(n), i + 1))))
    a -= set(range(0, 2))
    for i in range(2, int(max(a) ** 0.5) + 1):
        a -= set(range(i * 2, max(a) + 1, i))
    return len(a)