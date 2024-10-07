# 직사각형을 만드는 데 필요한 4개의 점 중 3개의 좌표가 주어질 때, 나머지 한 점의 좌 표를 구하려고 합니다. 점 3개의 좌표가 들어있는 배열 V가 매개변수로 주어질 때, 
# 직 사각형을 만드는 데 필요한 나머지 한 점의 좌표를 retum 하도록 soluton 함수를 완 성해주세요. 
# 단, 직사각형의 각 변은 x축, y축에 평행하며, 반드시 직사각형을 만들 수 있는 경우만 입력으로 주어집니다.

# 제한사항
# •v는 세 점의 좌표가 들어있는 2차원 배열입니다.
# • V의 각 원소는 점의 좌표를 나타내며, 좌표는 [x축 좌표, y축 좌표] 순으로 주어 집니다.
# • 좌표값은 1 이상 10억 이하의 자연수입니다.
# • 직사각형을 만드는 데 필요한 나머지 한 점의 좌표를 [X축 좌표, y축 좌표] 순으 로 담아 return 해주세요.

# 행, 열 중에 값이 하나인 것 찾기

from collections import Counter

v = [[1,4],[3,4],[3,10]]

count_row = Counter([v[i][0] for i in range(len(v))])
count_col = Counter([v[i][1] for i in range(len(v))])


        
print(count_row.most_common()[-1][0], count_col.most_common()[-1][0])

# GPT 풀이 

def solution(v):
    x_coords = [point[0] for point in v]
    y_coords = [point[1] for point in v]
    
    # x 좌표와 y 좌표에서 고유한 값을 찾기
    x = 0
    y = 0
    
    for x_coord in x_coords:
        x ^= x_coord  # XOR 연산을 사용하여 유일한 x 좌표 찾기
        
    for y_coord in y_coords:
        y ^= y_coord  # XOR 연산을 사용하여 유일한 y 좌표 찾기
    
    return [x, y]

# 예시
v = [[1, 4], [3, 4], [3, 10]]
result = solution(v)
print(result)  # [1, 10]
