# TODO: 2072. 홀수만 더하기

N = int(input())


for j in range(1,N+1):
    sum_num = 0 
    num_list = list(map(int, input().split(' ')))
    for i in num_list :
        if i %2 != 0 :
            sum_num += i 

    print(f"#{j} {sum_num} ")

    