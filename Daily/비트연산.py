# [ ] 비트 연산에 대해 공부하고 문제를 풀어보자

# [1] 배열의 길이를 2의 거듭제곱으로 만들기
# https://school.programmers.co.kr/learn/courses/30/lessons/181857
# https://www.youtube.com/watch?v=4BSrpZlGW4A

'''
point 1) n &(n-1) == 0이라면, n은 2의 배수임을 의미한다.
n이 2의 거듭제곱이라면, 2진수로 표현시 딱 한 비트만 1이된다. 
예를 들어 8은 1000(2), 32는 100000(2)가 된다. 이 때, -1은 한다면 현재 1인 비트가 0으로 바뀌고, 그 아래 0이였던 비트들이 모두 1로 변한다.
예를 들어 7은 0111(2), 32는 011111(2)가 된다. 따라서 각 자릿수의 비트 값이 반대가 된다(0/1) 그러니 두 비트가 모두 1일 때 1이되는 & 연산 결과가 무조건 0이 나온다.
즉 n&(n-1) == 0 이라면, n는 2의 거듭제곱이다.

point 2) n<<1 은 비트는 왼쪽으로 한 칸씩 옮기는 것으로 2배 해주는 결과가 된다.
예를 들어 4는 100(2), 100(2)<< 1 1000(2) 즉 8이 된다.

'''

def next_power_of_two(n):
    # n이 2의 거듭제곱인지 확인
    if n & (n-1) == 0 :
        return n
    # n이 2의 거듭제곱이 아니라면
    next_power = 1
    # n 이상의 2의 거듭제곱이 되었을 때,while문 빠져나옴
    while next_power < n:
        next_power <<= 1 # n보다 큰 2의 거듭 제곱을 찾을 때까지 2 곱하기
    
    return next_power

def solution(arr):
    length = len(arr)
    result_len = next_power_of_two(length)
 
    return arr + [0]*(result_len-length)

print(solution([2,2,2,2]))