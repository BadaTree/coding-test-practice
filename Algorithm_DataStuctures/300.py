# [ ] 300 수학 1

# [1] 나머지
'''
A, B, C = map(int, input().split())

# (A + B) % C 계산
result1 = (A + B) % C

# ((A % C) + (B % C)) % C 계산
result2 = ((A % C) + (B % C)) % C

# (A * B) % C 계산
result3 = (A * B) % C

# ((A % C) * (B % C)) % C 계산
result4 = ((A % C) * (B % C)) % C

# 결과 출력
print(result1)
print(result2)
print(result3)
print(result4)
'''

# [2] 최대 공약수와 최소 공배수
'''
def GCD(a,b):
    while b != 0:
        a,b = b , a % b
    return a 

def lcm(a,b, gcd_value):
    return (a*b) // gcd_value

a,b = map(int,input().split())

gcd_value = GCD(a,b)
lcm_value = lcm(a,b,gcd_value)

print(gcd_value)
print(lcm_value)
'''
        

# [3] 최소 공배수
'''
def GCD(a,b):
    while b != 0 :
        a,b = b, a%b
    return a

N = int(input())
for i in range(N):
    a,b = map(int,input().split())
    gcd = GCD(a,b)
    print((a*b)//gcd)
'''

# [4] 소수 찾기
N = int(input())
nums = list(map(int,input().split()))

count = 0

for num in nums :
    if num == 1 :
        pass
    else :
        n = 0
        for i in range(2,int(num**0.5)+1):
            if num % i == 0 :
                n += 1
                break
        if n == 0 :
            count += 1     
        
print(count)
# GPT 풀이

# [5] 소수 구하기
N = int(input())  # 입력받은 수의 개수
nums = list(map(int, input().split()))  # 숫자 리스트

count = 0  # 소수 개수를 셀 변수

for num in nums:
    if num < 2:  # 1이나 0은 소수가 아니므로 제외
        continue
    is_prime = True  # 소수 여부를 체크하는 변수
    for i in range(2, int(num ** 0.5) + 1):  # 제곱근까지만 나눠서 확인
        if num % i == 0:  # 나눠 떨어지면 소수가 아님
            is_prime = False
            break
    if is_prime:  # 소수일 경우 count 증가
        count += 1

print(count)  # 최종 소수 개수 출력

# [6] 골드바흐의 추측

# [7] 팩토리얼Add

# [8] 팩토리얼 0의 개수

# [9] 조합 0의 개수