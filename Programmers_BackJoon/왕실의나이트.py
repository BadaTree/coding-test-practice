#TODO: 왕실의 나이트

#CHECKLIST: 
#[x]: 띄어쓰기로 구분되지 않고 입력되는 x,y 어떻게 분리? 
# input = input()
# input[0], input[1]과 같이 호출
#[x]: 문자열로 입력되는 인덱스 어떻게 숫자로 변환
# column = int(ord(input_data[0])) - int(ord('a')) + 1
#[x]: 두 개의 리스트 사용하지 않고, 나이트가 이동할 수 있는 방향 8가지 정의
# steps = [(-2,-1),(-1,-2),(1,-2),(2,-1),(2,1),(1,2),(-1,2),(-2,1)]

#[ ] Code i wrote
input = input()

count = 0
# 나이트가 이동할 수 있는 방향 8가지 정의
dy = [-2,-2,-1,+1,+2,+2,-1,+1]
dx = [-1,+1,+2,+2,-1,+1,-2,-2]

# 입력 받은 인덱스 변환
ini_x = int(input[1])
index_y = ['a','b','c','d','e','f','g','h']
for i in range(len(index_y)) :
    if input[0] == index_y[i]:
        ini_y = i + 1
        
# 8가지 방향에 대해 이동 가능한지 확인
for i in range(8):
    nx = ini_x + dx[i]
    ny = ini_y + dy[i]
    
    if nx >0 and ny> 0 and nx <9 and ny <9:
        count += 1
        
print(count)

#[ ] Answer code
input_data = input()
row = int(input[1])
column = int(ord(input_data[0])) - int(ord('a')) + 1

# 나이트가 이동할 수 있는 방향 8가지 정의
steps = [(-2,-1),(-1,-2),(1,-2),(2,-1),(2,1),(1,2),(-1,2),(-2,1)]

# 8가지 방향에 대해 이동 가능한지 확인
result = 0
for step in steps:
    n_row = row + step[0]
    n_column = column + step[1]

    if n_row >0 and n_column> 0 and n_row <9 and n_column <9:
        result += 1
print(result)