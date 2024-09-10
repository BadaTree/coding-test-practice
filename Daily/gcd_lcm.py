# TODO : 최대공약수와 최소공배수를 정복해보자
# https://velog.io/@forntweb_tk/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EC%B5%9C%EB%8C%80%EA%B3%B5%EC%95%BD%EC%88%98%EC%99%80-%EC%B5%9C%EC%86%8C%EA%B3%B5%EB%B0%B0%EC%88%98-Python


# [ ] 최대 공약수 (GCD)
# 두 정수가 n과 m이고, n을 m으로 나눈 나머지가 r일 때, 
# n과 m의 최대공약수는 m과 r의 최대공약수와 같다.

def GCD(n,m):
    if m == 0:
        return n
    else:
        return GCD(m, n%m)
        
GCD(12,15)
    
# [ ] 최소 공배수 (lcm) (n,m)
# n = GCD*a, m = GCD*b
# lcm = GCD*a*b
# lcm = n*m/GCD

import math

def lcm(n,m):
    return n*m / GCD(n,m)

print(lcm(5,15),math.lcm(5,15))