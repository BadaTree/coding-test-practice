# [ ] Sort
# https://www.youtube.com/watch?v=KGyK-pNvWos&t=949s

# [1] 정렬이란?
# 데이터를 특정한 기준에 따하 순서대로 나열하는 것을 의미.
# 일반 적으로 문제 상황에 따라서 적절한 정렬 알고리즘이 공식처럼 사용됩니다.
# 예) 데이터가 적거나 많지만 범위가 한정되어있을때 정해진 알고리즘을 이용해 정렬한다.


# [2] 선택 정렬 O(N^2)
 # 처리되지 않은 데이터 중 가장 작은 데이터를 선택해서 맨 앞에 데이터와 바꾸는 것을 반복.
'''
array = [7,5,9,0,3,1,6,2,4,8]

for i in range(len(array)):
    min_index = i
    for j in range(i+1,len(array)):
        if array[min_index] > array[j]:
            min_index = j
            
    array[min_index], array[i] = array[i], array[min_index] 
    
print(array)
'''

# [3] 삽입 정렬 O(N^2)
# 현재 리스트의 데이터가 정렬되어 있을수록 빠르게 동작 (연산 수 비례)
# 처리되지 않은 데이터를 하나씩 골라 적절한 위치에 삽입합니다. (오름차순 정렬 전제)
# 선택 정렬에 비해 구현 난이도가 높은 편이지만, 일반적으로 더 효율적으로 동작합니다.

'''
from collections import deque

array = [7,5,9,0,3,1,6,2,4,8]

for i in range(1,len(array)): # 인덱스 i부터 그 앞 원소들과 대소 비교하며 정렬
    for j in range(i,0,-1): # 한 칸씩 왼쪽으로 이동하며 정렬
        if array[j-1] > array[j]:
            array[j-1], array[j] = array[j], array[j-1]
        else : # 앞 원소가 비교 원소보다 작을 때 정렬 종료 
            break 
        
print(array)
'''

# [4] 퀵 정렬 평균 O(NlogN), 최악의 경우: 이미 정렬된 배열  O(N^2)
# 일반적인 상황에서 가장 많이 사용되는 정렬 알고리즘 중 하나.
# 피벗을 기준으로 데이터 묶음을 나누는 작업을 분할(Divide)이라고 합니다.
# 피벗을 기준으로 작은 값, 큰 값을 분리해 나가면서 재귀적으로 정렬. 
# 그 분리 묶음원소가 작아져 한 개 이하가 되었을 때 정렬 완료를 의미
# 기준 데이터를 설정하고, 그 기준보다 큰 데이터와 작은 데이터의 위치를 바꾸는 방법
# 병합 정렬과 더불어 대부분의 프로그래밍 언어의 정렬 라이브러리 근간이 되는 알고리즘
# 기본적인 퀵 정렬은 첫 번째 데이터를 기준 데이터로 설정하고 시작한다.

# 일반적인 방식
'''
array = [5,7,9,0,3,1,6,2,4,8]

def quick_sort(array, start, end):
    if start >= end : # 원소가 1개인 경우 종료 
        return
    pivot = start # 피벗은 첫 번째 원소
    left = start + 1
    right = end
    
    while(left <= right): # 엇갈릴 때까지 반복
        # 피벗보다 왼쪽 끝에서부터 오른쪽 끝까지(left <=end) 피벗보다 큰 데이터를 찾을 때까지 반복
        while (left <=end and array[left] <= array[pivot]):
            left += 1
        # 피벗보다 오른쪽 끝에서부터 왼쪽 끝까지(right > start) 피벗보다 작은 데이터를 찾을 때까지 반복
        while (right > start and array[right] >= array[pivot]):
            right -= 1
        if left > right : # 엇갈렸다면 작은 데이터와 피벗을 교체 
            array[right], array[pivot] = array[pivot], array[right]
        else : # 엇갈리지 않았다면 작은 데이터와 큰 데이터를 교체 
            array[left],array[right] = array[right], array[left]
    
    # 분할 이후에 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행 
    quick_sort(array, start, right-1)
    quick_sort(array, right+1, end)
    

quick_sort(array, 0 , len(array)-1)
print(array)
'''

# 파이썬의 장점을 살린 방법
'''
array = [5,7,9,0,3,1,6,2,4,8]

def quick_sort(array):
    # 리스트가 하나 이하의 원소만 담고 있다면 종료 (= 해당 영역 정렬 완료)
    if len(array)<=1:
        return array
    
    pivot = array[0] # 피벗은 첫 번째 원소
    tail = array[1:] # 피벗을 제외한 리스트 
    
    left_array = [x for x in tail if x <= pivot] # 분할된 왼쪽 부분
    right_array = [x for x in tail if x > pivot] # 분할된 오른쪽 부분

    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행하고, 전체 리스트 반환
    return quick_sort(left_array)+ [pivot] + quick_sort(right_array)

print(quick_sort(array))
'''

# [5] 계수 정렬 O(N+K)
# 계수 정렬은 동일한 값을 가지는 데이터가 여러 개 등장할 때 효과적으로 사용가능!

# 특정한 조건이 부합할 때만 사용할 수 있지만 매우 빠르게 동작하는 정렬 알고리즘.
# 계수 정렬은 데이터의 크기 범위가 제한되어 정수 형태로 표현할 수 있을 때 사용 가능하다.
# 데이터의 개수가 N, 데이터(양수) 중 최댓값이 K일 때 최악의 경우에도 수행 시간 O(N+K)를 보장한다.
# 인덱스 : 데이터의 값, 값: 데이터의 빈도 수 
'''
# 모든 원소의 값이 0보다 크거나 같다고 가정
array = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2 ]
# 모든 범위를 포함하는 리스트 선언 (모든 값은 0으로 초기화)
count_list = [0]*(max(array)+1)

# 데이터의 갯수 카운트 데이터 값에 해당하는 인덱스의 값 +1
for i in array:
    count_list[i] += 1 # 각 데이터에 해당하는 인덱스의 값 증가 
    
for i in range(len(count_list)): # 리스트에 기록된 정렬 정보 확인
    for j in range(count_list[i]):
        print(i, end=' ' ) # 띄어쓰기를 구분으로 등장한 횟수만큼 인덱스 출력 
'''
   
# [ ] 선택 정려과 기본 정렬 라이브러리 수행 시간 비교
'''
from random import randint
import time 

# 배열에 10,000개의 정수를 삽입 
array = []
for _ in range(10000):
    # 1부터 100사이의 랜덤한 정수 
    array.append(randint(1,100))
    
# 선택 정렬 프로그램 성능 측정
start_time = time.time()

# 선택 정렬 프로그램 소스 코드
for i in range(len(array)):
    min_index = i # 가장 작은 원소의 인덱스
    for j in range(i+1, len(array)):
        if array[min_index] > array[j]:
            min_index = j
    array[i], array[min_index] = array[min_index], array[i]
    
# 측정 종료
end_time = time.time()
# 수행 시간 출력
print('선택 정렬 성능 측정:', end_time - start_time)
    
# 배열에 10,000개의 정수를 삽입 
array = []
for _ in range(10000):
    # 1부터 100사이의 랜덤한 정수 
    array.append(randint(1,100))
    
# 기본 정렬 프로그램 성능 측정
start_time = time.time()

# 기본 정렬 라이브러리 사용
array.sort()

# 측정 종료
end_time = time.time()

# 수행 시간 출력 
print("기본 정렬 라이브러리 성능 측정:",end_time-start_time)
 '''
# [ ] sort 기본 문제 풀이하기 
# A는 최소부터 B는 최대부터 바꿔치기하기
# a의 최소값이 b의 최대값보다 큰 경우 교체시 a합이 더 작아지므로 교체를 멈춰야함 

# quick 정렬 정의
def quick_sort (array):
    if len(array) <=1:
        return array
    
    pivot = array[0]
    array_ = array[1:]
    
    left_array = [i for i in array_ if pivot > i]
    right_array = [i for i in array_ if pivot < i]
    
    return quick_sort(left_array) + [pivot] + quick_sort(right_array)

# 계수정렬 정의
def sorted(array):
    answer = []
    temp_array = [0]*(max(array)+1)
    
    for i in array:
        temp_array[i] += 1
        
    for i in range(len(temp_array)):
        for j in range(temp_array[i]):
            answer.append(i)
    return answer

N, K = map(int,input().split())
A_arr = list(map(int,input().split()))
B_arr = list(map(int,input().split()))
a = A_arr
b = B_arr

# A,B 정렬
A_arr = sorted(A_arr)
B_arr = sorted(B_arr)

for i in range(K):
    A_arr[i],B_arr[N-i-1] = B_arr[N-i-1],A_arr[i]
    
print("바다 풀이 답 :",sum(A_arr))

# 정답 풀이
a.sort() # a는 오름차순 정렬
b.sort(reverse=True)# b는 내림차순 정렬

for i in range(K): # K번 바꿔치기 수행
    if a[i] < b[i]:
        a[i],b[i] = b[i], a[i]
    # a의 최소값이 b의 최대값보다 큰 경우 교체시 a합이 더 작아지므로 교체를 멈춰야함 
    else: ## a의 최소값이 b의 최대값보다 작거나 같으면 합이 더 작아지거나 의미없음 
        break 
    
print("정답 풀이: ",sum(a))
