# TODO: 4861. [파이썬 S/W 문제해결 기본] 3일차 - 회문

T = int(input())


for i in range(1,T+1):
    N,M = list(map(int, input().split(' ')))
    Area = [[0]*M for _ in range(N)]
    result = ""
    found = False

    # 문자열 입력 받기 
    for j in range(N):
        Area[j][:] = list(input())
    
    # 가로 먼저 검사 
    if N %2 == 0:
        for r in range(N):
            mid = M//2 
            count = 0
            for m in range(mid):
                if Area[r][mid-1-i] != Area[r][mid+i]:
                    break
                else : 
                    count += 1
            if mid == count : 
                result = Area[r][:]
                found = True

    # 세로 먼저 검사 
    if  not found:
        for r in range(M):
            mid = N//2 
            count = 0
            for m in range(mid):
                if Area[mid-1-i][r] != Area[mid+i][r]:
                    break
                else : 
                    count += 1
            if mid == count : 
                result = Area[:][r]
                found = True
                
    print(f"#{i} {''.join(result)}")


# [ ] 오류 지피티로 수정
'''
코드에서 오류를 수정해보겠습니다.

가로와 세로를 모두 검사하여 회문을 찾아야 합니다. 그러나 코드에서는 가로나 세로 중 하나만 검사합니다. 따라서 둘 다 검사할 수 있도록 수정해야 합니다.
회문의 길이가 M인데, 가로로 검사할 때 M//2부터 시작해서 M-1까지만 검사해야 합니다. 현재 코드에서는 M에 따라 범위를 동적으로 설정하지 않고 고정된 범위로만 검사합니다.
세로로 검사할 때 result에 할당하는 부분이 올바르지 않습니다. 리스트의 슬라이싱을 사용하여 수정해야 합니다.
다음은 수정된 코드입니다.

python
Copy code
T = int(input())

for i in range(1, T+1):
    N, M = map(int, input().split())
    Area = [input() for _ in range(N)]
    result = ""
    found = False

    # 가로 검사
    for r in range(N):
        for c in range(N - M + 1):  # M길이의 회문을 검사하기 위해 범위 조정
            if Area[r][c:c+M] == Area[r][c:c+M][::-1]:  # 회문인 경우
                result = Area[r][c:c+M]
                found = True
                break
        if found:
            break
    
    # 세로 검사
    if not found:
        for c in range(N):
            for r in range(N - M + 1):  # M길이의 회문을 검사하기 위해 범위 조정
                column = ''.join(Area[r:r+M][k][c] for k in range(M))  # 세로 부분 문자열 생성
                if column == column[::-1]:  # 회문인 경우
                    result = column
                    found = True
                    break
            if found:
                break

    print(f"#{i} {result}")
이 코드는 주어진 NxN 크기의 글자판에서 길이가 M인 회문을 찾아 출력합니다. 가로와 세로를 모두 검사하여 회문을 찾습니다.
'''