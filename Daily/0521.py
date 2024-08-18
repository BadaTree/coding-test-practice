# TODO: Programmers 문제 풀고, 정리 노트 작성하기 
# NOTE: 꼭 아래 코드 이해하고 재 풀이 해 보기 !!

#[ ] 1. n의 배수 고르기 

'''정수 n과 정수 배열 numlist가 매개변수로 주어질 때, numlist에서 n의 배수가 아닌 수들을 제거한 배열을 return하도록 solution 함수를 완성해주세요.'''

def solution(n, numlist):
    return list(filter(lambda v: v%n==0, numlist))




# [ ] 2. 부분 문자열 이어 붙여 문자열 만들기
'''길이가 같은 문자열 배열 my_strings와 이차원 정수 배열 parts가 매개변수로 주어집니다. parts[i]는 [s, e] 형태로, my_string[i]의 인덱스 s부터 인덱스 e까지의 부분 문자열을 의미합니다. 각 my_strings의 원소의 parts에 해당하는 부분 문자열을 순서대로 이어 붙인 문자열을 return 하는 solution 함수를 작성해 주세요.'''
def solution(my_strings, parts):
    return ''.join([x[y[0]:y[1]+1] for x,y in zip(my_strings, parts)])


# [ ] 3. 주사위 게임 1
'''1부터 6까지 숫자가 적힌 주사위가 두 개 있습니다. 두 주사위를 굴렸을 때 나온 숫자를 각각 a, b라고 했을 때 얻는 점수는 다음과 같습니다.

a와 b가 모두 홀수라면 a2 + b2 점을 얻습니다.
a와 b 중 하나만 홀수라면 2 × (a + b) 점을 얻습니다.
a와 b 모두 홀수가 아니라면 |a - b| 점을 얻습니다.
두 정수 a와 b가 매개변수로 주어질 때, 얻는 점수를 return 하는 solution 함수를 작성해 주세요.'''

def solution(a, b):
        return a*a+b*b if a & b & 1 else (a + b) << 1 if (a | b) & 1 else abs(a - b)

# [ ] 4. 꼬리 문자열
'''문자열들이 담긴 리스트가 주어졌을 때, 모든 문자열들을 순서대로 합친 문자열을 꼬리 문자열이라고 합니다. 꼬리 문자열을 만들 때 특정 문자열을 포함한 문자열은 제외시키려고 합니다. 예를 들어 문자열 리스트 ["abc", "def", "ghi"]가 있고 문자열 "ef"를 포함한 문자열은 제외하고 꼬리 문자열을 만들면 "abcghi"가 됩니다.

문자열 리스트 str_list와 제외하려는 문자열 ex가 주어질 때, str_list에서 ex를 포함한 문자열을 제외하고 만든 꼬리 문자열을 return하도록 solution 함수를 완성해주세요.'''

def solution(str_list, ex):
    return ''.join(filter(lambda x: ex not in x, str_list))

# [ ] 5. 0 떼기
'''
정수로 이루어진 문자열 n_str이 주어질 때, n_str의 가장 왼쪽에 처음으로 등장하는 0들을 뗀 문자열을 return하도록 solution 함수를 완성해주세요.'''

def solution(n_str):
    return str(int(n_str))
def solution(n_str):
    return n_str.lstrip('0')


# [ ] 6. 배열 길이에 따라 다른 연산하기 
'''정수 배열 arr과 정수 n이 매개변수로 주어집니다. arr의 길이가 홀수라면 arr의 모든 짝수 인덱스 위치에 n을 더한 배열을, arr의 길이가 짝수라면 arr의 모든 홀수 인덱스 위치에 n을 더한 배열을 return 하는 solution 함수를 작성해 주세요.'''

# [num + n*((len(arr)+i)%2) for i, num in enumerate(arr)]

# def solution(arr, n):
#     return [arr[i] + n if i % 2 == 0 else arr[i] for i in range(len(arr))] if len(arr) % 2 != 0 else [arr[i] + n if i % 2 != 0 else arr[i] for i in range(len(arr))]
