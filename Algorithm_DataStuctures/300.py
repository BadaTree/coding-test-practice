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

        
    


# [3] 최소 공배수

# [4] 소수 찾기

# [5] 소수 구하기

# [6] 골드바흐의 추측

# [7] 팩토리얼Add

# [8] 팩토리얼 0의 개수

# [9] 조합 0의 개수