# TODO: Stack

# Stack은 선입 후출임을 명시하자 !, 그릇 쌓고 빼기 생각
# 추가는 append(), 빼내기는 pop()

#[ ] 재귀함수 성질 활용하여 팩토리얼 구현하기
def factorial(n,result):
    if n == 0 :
        print(result)
    else:
        result = result+f"{n}"
        n -= 1
        factorial(n, result)
        
a = factorial(5,"") 

# [ ] 재귀 호출로 피보나치 수열을 구현하기
# 피보나치 수열을 재귀함수로 구현시 호출 중복이 많아 수행시간이 너무 오래 걸림 
# -> 이를 해결하기 위해 메모이제이션을 활용하여 구현해야함

# NOTE: Memoization의 의미 : DP(동적계획법의 핵심이 되는 기술)
# 컴퓨터 프로그램을 실행할 때 이전에 계산한 값을 메모리에 저장해서 매번 
# 다시 계산하지 않도록 하여 전체적인 실행 속도를 빠르게하는 기술

# DP 동적계획 알고리즘 :