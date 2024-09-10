# TODO : 2차원 list

# [ ] 2차원 리스트 초기화하기

arr = [1,2,3]*3
print(f"1차원: {arr}")

arr = [[1,2,3]]*3 
print(f"2차원: {arr}")

arr1 = [i for i in range(8) if i%2==0 ]

brr = [[1,2,3] for i in range(3)]
brr1 = [[i,j] for i in range(3) for j in range(2)]
print(brr1)

# [ ] 2차원 list 입력받기
'''
n,m = map(int, input().split())
mylist = [0]*m
for _ in range(n):
    mylist = list(map(int, input().split()))
    
mylist1 = [list(map(int, input().split())) for _ in range(n)]

# [ ] 2차원 list에서 원하는 데이터 위치 찾기
answer = [(i,j) for i in range(n) for j in range(m) if mylist[i][j] == 1]
'''

# NOTE: 2차원 리스트의 모든 원소를 빠짐없이 조사하는 방법

arr = [[0,1,2,3],[4,5,6,7],[8,9,10,11],[12,13,14,15]]

# 행의 길이 
n = len(arr)
# 열의 길이 
m = len(arr[0])

# [ ] 행 우선 순회
for i in range(len(arr)):
    for j in range(len(arr[i])):
        arr[i][j]
        # print("행: ##",arr[i][j])
# [ ] 열 우선 순회 
for j in range(len(arr[0])):
    for i in range(len(arr)):
        arr[i][j]
        # print("열: &&",arr[i][j])
# [ ] 지그재그 순회
for i in range(len(arr)):
    for j in range(len(arr[i])):
        arr[i][j + (m - 1-2*j)*(i%2)]

# NOTE: 델타를 이용한 2차원 list 탐색

dx = [1,-1,0,0]
dy = [0,0,-1,1]

for x in range(len(arr)):
    for y in range(len(arr[0])):
        for i in range(4):
            testx = x + dx[i]
            testy = y + dy[i]
            # print(arr[testx][testy])
            
            
# NOTE: zip(literable*)
alpha = ['a','b']
num = [1,2,3,4]

# [ ] 두 개의 자료형 묶어주는 함수
print(list(zip(alpha,num)))

#[ ] 전치행렬 
print(list(zip(*arr)))