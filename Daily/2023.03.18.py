basket_global = []
basket_temp = []

N,M = input().split()
M = int(M)
N = int(N)

for i in range(N):
    basket_global.append(i+1)

for l in range(M):
    i,j,k = input().split()
    i = int(i)
    j = int(j)
    k = int(k)
    basket_temp = basket_global[k-1:j]
    basket_temp.extend(basket_global[i-1:k-1])
    basket_global[i-1: j] = basket_temp[:]
    basket_temp = []

print(*basket_global)


n = int(input())
for i in range(n):
    a, b = input().split()
    a = int(a)
    b = int(b)
    print(a+b)
