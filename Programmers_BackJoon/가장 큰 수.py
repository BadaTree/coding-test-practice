# TODO: Programmers 가장 큰 수 

def solution(numbers):
    numbers = list(map(str,numbers))
    numbers.sort(key= lambda x : x*3, reverse=True)
     
    answer = str(int(''.join(numbers)))
    return answer

answer= solution([3,30,34,5,9])
print(answer)