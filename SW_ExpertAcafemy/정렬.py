# TODO: 정렬 알고리즘

# 선택 정렬 구현하기 
arr = [1, 27, 3, 41, 31, 6, 7, 11]

for i in range(len(arr)):
    min_value = arr[i]
    min_index = i
    
    for j in range(i+1,len(arr)):
        if arr[j] < min_value:
            min_value = arr[j] # 기준 값 이후의 값에서 최솟값 찾아 갱신하기
            min_index = j

    arr[i], arr[min_index] = min_value, arr[i]
    
print(arr)