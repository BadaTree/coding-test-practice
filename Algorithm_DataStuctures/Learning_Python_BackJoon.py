
# [ ] BACKJOON 2530 

# [1]
clock = list(map(int,input().split(' ')))
T = int(input())

# 종료 시간 업데이트 
clock[0] += T//3600
clock[1] += (T %3600)//60
clock[2] += (T%3600)%60

# 시분초 정렬
if (clock[2] // 60)  >= 1:
    clock[1] += clock[2]//60
    clock[2] %= 60
    
if (clock[1] // 60 ) >= 1:
    clock[0] += clock[1] // 60
    clock[1] %= 60
    
if clock[0]>= 24 :
    clock[0]-= 24
# 23시 59분 59초     

print(clock)

# [2]
current_time = list(map(int, input().split()))
cooking_duration = int(input())

current_time_in_seconds = (current_time[0] * 3600) + (current_time[1] * 60) + current_time[2]

total_seconds = current_time_in_seconds + cooking_duration

print((total_seconds // 3600) % 24, (total_seconds % 3600) // 60, (total_seconds % 3600) % 60)
