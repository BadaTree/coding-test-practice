#TODO: 시각: 

#CHECKLIST: '3' in str(i)+str(j)+str(k)

N =int(input())
count = 0

for i in range(N+1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i)+str(j)+str(k):
                count += 1
print(count)
             
             
# NOTE: Why did I get this wrong?
# i % 3 == 0 or j%3 == 0 or k%3 ==0 // i / 3 == 0 or j/3 == 0 or k/3 ==0
#24, 48초와 같이 시각에 3이 포함되지 않지만 3으로 나누어지는 수가 포함되어 오류 발생!
count0,count1 = 0,0
for k in range(60):
    
    if '3' in str(k):
        count0 += 1
    if k % 3 == 0:
        count1 += 1
    # print(count0,count1)
    