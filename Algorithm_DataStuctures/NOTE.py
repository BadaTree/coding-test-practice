# 1시간 : 3600 1분 60 

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