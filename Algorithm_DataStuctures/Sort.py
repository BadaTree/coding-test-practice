# [ ] Sort

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

# [4] 퀵 정렬
