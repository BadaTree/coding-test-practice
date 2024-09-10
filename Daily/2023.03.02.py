## 2738 런타임에러 수정하기

a,b = map(int, input().split())

list_1 = [[0 for j in range(int(a))] for i in range(int(b))]
list_2 = [[0 for j in range(int(a))] for i in range(int(b))]
final_list = [[0 for j in range(int(a))] for i in range(int(b))]
temp_1 = [0 for i in range(int(b))]
temp_2 = [0 for i in range(int(b))]

for i in range(int(a)):
    temp_1 = input().split()
    for j in range(int(b)):
        value = int(temp_1[j])
        list_1[i][j] = value
for i in range(int(a)):
    temp_2 = input().split()
    for j in range(int(b)):
        value = int(temp_2[j])
        list_2[i][j] = value
        final_list[i][j] = list_1[i][j] + value
for i in range(int(a)):
    print(final_list[i][:])