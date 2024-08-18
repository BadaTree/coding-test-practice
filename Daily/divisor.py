# [ ] 약수 계산 효율적으로 하기 
# 약수는 대칭적으로 발생한다는 특징을 활용하여 제곱근까지 연산하여, 대칭하는 두 개의 약수를 한번에 찾기
# 예 : 36 약수를 찾을 때, 36%2 = 0 이므로 2와 36//2 = 18을 한번에 찾을 수 있음.
# NOTE: 단 중복이 발생할 수 있으니 확인 필수 
# 예 : 36 약수를 찾을 때, 36 % 6 = 6과 36//6 = 6으로 대칭하는 약수가 중복되므로 이 경우는 필터링 해줘야함. 


#[1] Q. 자연수 N의 약수를 오름차순으로 출력하시오.

# WORST: For문으로 1~N까지 계산하며 약수찾기
def get_divisor(num):
    result = []
    for i in range(1,N+1):
        if num % i == 0:
            result.append(i)
    return result

N = 36
print("Words:", get_divisor(N))

# BEST : 약수는 대칭적으로 발생한다는 특징을 활용하여 제곱근까지 연산하기
def get_divisor(num):
    result = []

    for i in range(1,int(N**0.5)+1):
        if N % i == 0:
            result.append(i)
            if i != N//i: # 중복되는 약수인지 확인 예)  N % i= 6,N//i =6
                result.append(N//i) 
    return sorted(result)

N = 36
print("BEST:", get_divisor(N))


# [2] Q. 약수의 개수가 세 개 이상인 수를 합성수라고 합니다. 
# 자연수 n이 매개변수로 주어질 때 n이하의 합성수의 개수를 return하도록 solution 함수를 완성해주세요.

# WORST: 이중 For문으로 1~N까지 계산하며 합성수인지 찾기
def solution(n):
    count = 0
    for i in range(1, n+1):
        if sum([1 for j in range(1, i+1) if i% j == 0]) >= 3:
            count += 1
    return count

N= 36
print("WORST:", solution(N))

# BEST : 약수는 대칭적으로 발생한다는 특징을 활용하여 
# 제곱근의 약수의 갯수가 2개 이상이면 전체 약수의 갯수가 최소 3개 이상이므로 합성수임을 판단할 수 있다.
# 제곱근의 약수가 2개 이상이 될 때 합성수임을 판단하여 , 효율적으로 합성수 찾기

def is_composite(num):
    count = 0
    for i in range(1, int(num**0.5)+1):
        if num % i == 0 and i != num // i :
            count += 2
        elif num % i == 0 :
            count += 1
        # 제곱근의 약수가 2개라면 전체 약수가최소 3개 이상이 되므로 합성수임
        # 합성수임이 판단되면 연산 중단 (약수가 3개 이상)
        if count >= 3: 
            return True
    return False


N = 36
def solution(N):
    count = 0
    for i in range(1,N+1):
        if is_composite(i):
            count += 1
    return count
print("BEST:", solution(N))