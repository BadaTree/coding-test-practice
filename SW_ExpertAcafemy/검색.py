# TODO: 검색

# [ ] 순차 검색 O(N)
# 일렬로 되어 있는 자료를 순서대로 검색하는 방법
# List나 연결 List 등 순차구조로 구현된 자료구조에서 유용함
# 구현이 쉽지만, 검색 대상이 많은 경우 수행시간의 증가로 비효율적임 

# [ ] 이진 검색 O(logN)
# 이진 검색을 하기 위해서는 자료가 정렬된 상태여야 한다.
# 자료의 가운데 항목의 키 값과 비교하여 다음 검색의 위치를 결정하고 검색을 계속하는 방법
# 목적 키를 찾을 때까지 이진 검색을 반복하여 검색 범위를 반으로 줄여가며 빠르게 검색 수행




# while start <= end:
#     middle = start + (end-start)//2
#     if arr[middle] == key : # 검색 성공
#         print(middle)
#     elif arr[middle] > key: # 키 값보다 중앙 값이 클 때, 왼쪽 재검색
#         end = middle - 1 
#     elif arr[middle] < key: # 키 값보다 중앙 값이 작을 때, 오른쪽 재검색
#         start = middle + 1 

# [ ] 재귀함수로 구현

def Search(arr,key, start,end):
    if start > end: # 검색 실패
        print("f")
        return False
    else:
        middle = (start + end) //2
        if arr[middle] == key : # 검색 성공
            print(middle,"성공")
            return True
            
        elif arr[middle] > key: # 키 값보다 중앙 값이 클 때, 왼쪽 재검색
            end = middle - 1 
            return Search(arr,key, start,end)
        elif arr[middle] < key: # 키 값보다 중앙 값이 작을 때, 오른쪽 재검색
            start = middle + 1 
            return Search(arr,key, start,end)

arr = [2,3,35,7,9,14,27,22]
key = 14
arr.sort() # 이진 검색은 자료가 정렬된 상태에서만 정상 동작

start = 0 
end = len(arr)-1 #인덱스는 0부터 시작하므로 최대 인덱스는 -1
result = Search(arr,key, start,end)
print(result)

#[ ] 인덱스 