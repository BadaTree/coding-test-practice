# [ ] IT기업 및 대기업 계열사 코테보면서 비슷했던 문제들
# https://www.acmicpc.net/workbook/view/8708

# [ ] 2292 벌집

def find_min_steps(N):
    if N == 1:
        return 1  # 1번 방은 이미 중앙에 있으므로 1칸
    
    layer = 1  # 벌집의 층 (최소 1부터 시작)
    count = 1  # 방 개수를 카운트 (중앙은 1번 방이므로 처음은 1)

    # 벌집의 방들이 1, 7, 19, 37, 61... 과 같은 수열로 형성되므로
    # 다음 조건을 통해 N이 어느 레이어에 속하는지 찾음
    while N > count:
        count += 6 * layer  # 각 층마다 6개씩 방이 추가됨
        layer += 1
    
    return layer

# 입력 받기
N = int(input())
print(find_min_steps(N))
