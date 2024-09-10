# 이것이 코딩 테스트다 with python, 15강 구현 문제 풀이

# Q. 정수 N이 입력되면 00시 00분 00초부터 N시 59분 59초까지의 모든 시각 중에서 3이 하나라도 포함되는 모든 경우의 수를 구하는 프로그램을 작성하세요.

# h,m,s를 문자열로 받아와서 count하는 방식
hour = int(input())
count = 0
for i in range(hour+1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i)+str(j)+ str(k):
                count += 1

print(count)

# h,m,s 를 숫자로 받아와서 count하는 방식

hour = int(input())
count = 0
for i in range(hour+1):
    for j in range(60):
        for k in range(60):
            if  i % 10 ==3 or j/10 == 3 or j % 10 == 3 or k/10 == 3 or k % 10 == 3:
                count += 1

print(count)

# Q. 왕실의 나이트 : 나이트는 말을 타고 있기 때문에 이동할 때는 L자이 형태로만 이동할 수 있다.
# 1. 수평으로 두 칸 이동한 뒤에 수직으로 한 칸 이동하기
# 2. 수직으로 두 칸 이동한 뒤에 수평으로 한 칸 이동하기
# 행 위치 표현은 1 부터 8로 표현하고, 열의 위리는 a부터 h로 표현한다.

