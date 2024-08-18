# array = [1, 2, 3, 4, 5]
# array.sort()
# index = len(array)//2
# print(array[index])

# Problem: 첫 번째 분수의 분자와 분모를 뜻하는 numer1, denom1, 
# 두 번째 분수의 분자와 분모를 뜻하는 numer2, denom2가 매개변수로 주어집니다. 두 분수를 더한 값을 기약 분수로 나타냈을 때 분자와 분모를 순서대로 담은 배열을 return 하도록 solution 함수를 완성해보세요.

from collections import Counter

def modefinder(numbers):   #numbers는 리스트나 튜플 형태의 데이터
    c = Counter(numbers)
    print(c)
    if len(c) >= 2:
        mode = c.most_common(2)
        if mode[0][1] == mode[1][1] :
            return -1
        else: 
            return mode[0][0]
    else :
        mode = c.most_common(1)
        return mode[0][0]

result = modefinder([1, 2, 3, 3, 3, 4])
print(result)
