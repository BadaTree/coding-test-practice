# TODO : 24.07.06 데일리 코딩 문제를 풀어보자
# [ ] 백준 1181

import sys

input = sys.stdin.read().splitlines()
words = []

# 입력 단어와 단어 길이 차례대로 저장 
N = int(input[0])

for i in range(1, N + 1):
    word = input[i]
    words.append(word)

# 중복 단어 제거
words = list(set(words))

# 단어 길이-> 사전 순서대로 정렬
# NOTE: 아래 정렬방식 익히기
word.sort(key=lambda x : (len(x),x))

# 정렬된 단어 출력
for word in words:
    print(word)

# TODO : 24.07.07 데일리 코딩 문제를 풀어보자

# [ ] 프로그래머스 3진법 뒤집기 
# NOTE: N진법 변환하는 것 공부하기
# https://school.programmers.co.kr/learn/courses/30/lessons/68935


# [ ] 짝지어 제거하기
# https://school.programmers.co.kr/learn/courses/30/lessons/12973