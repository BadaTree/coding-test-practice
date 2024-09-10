# # TODO: DFS & BFS 기본 개념


# #[ ] 스택 자료 구조
# #[x]: 먼저 들어온 데이터가 나중에 나가는 자료구조 (선입 후출)
# # Python에서는 list의 .append, pop을 이용해서 스택 구현 가능
# # 박스를 쌓아올리는 모습 상상하기!

# list = []

# list.append(5)
# list.append(2)
# list.append(3)
# list.append(7)
# list.pop()
# list.append(1)
# list.append(4)
# list.pop()

# print(list[::-1]) # 최상단 원소부터 출력
# print(list) #최하단 원소부터 출력


# # [ ] 큐 자료구조
# #[x]: 먼저 들어 온 데이터가 먼저 나가는 형식(선입선출)의 자료구조이다.
# # 대기열에 줄 선대로 차례대로 나가는 모습 상상!

# from collections import deque

# # 큐 구현을 위해 deque 라이브러리 사용
# queue = deque()

# # 삽입(5) - 삽입(2) - 삽입(3) - 삽입(7) - 삭제 - 삽입(1) - 삽입(4) - 삭제 ()
# queue.append(5)
# queue.append(2)
# queue.append(3)
# queue.append(7)
# queue.popleft()
# queue.append(1)
# queue.append(4)
# queue.popleft()

# print(queue) # 들어온 순서대로 deque([3, 7, 1, 4])
# queue.reverse
# print(queue) # 나중에 들어온 순서대로 출력 deque([3, 7, 1, 4])


# # [ ] 재귀 함수(Recursive Function)란 자기 자신을 다시 호출하는 함수를 의미. 
# # 자기 자신을 함수 정의 안에서 호출하여 무한히 출력
# # while이나 for문 사용하지 않고도 반복 가능
# # 재귀함수를 문제 풀이에서 사용할 때는 종료 조건을 반드시 명시해야 한다.
# # 종료 조건을 반드시 포함해야함!! 
# # 스택에 데이터를 담고 뽑아내는 것처럼 선입후출 구조.

# def recursive_fun(i):
#     if i == 100:
#         return
#     print(f"{i}함수가 {i+1}번째 함수를 호출합니다!")
#     recursive_fun(i + 1)
#     print(f"{i}번쨰 재귀함수를 종료합니다")

# recursive_fun(1)


# #[ ] 재귀함수를 이용항 팩토리얼 구현하기 

# def pat(n):
#     result = 1
#     for i in range(1,n+1):
#         result *= i
#     return result
    
# def recursive(n):
#     if n < 1:
#         return 1
#     return n*recursive(n-1)
# print("반복 :" ,pat(5))
# print("재귀 :" ,recursive(5))


#[ ] 재귀함수를 이용하여 최대공약수 계산 (유클리드 호제법) 예제
# 재귀함수를 잘 활용하면 복잡한 알고리즘을 간결하게 작성할 수 있다.
# 연속 호출시 스택 프레임에 쌓이는 것을 방지하여 재귀를 이용하는 경우가 많다.
def GCD(a,b):
    if a % b == 0 :
        return b
    else:
        return GCD(b, a%b)
    
print(GCD(192,162))