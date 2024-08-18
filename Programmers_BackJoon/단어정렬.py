# TODO: [구현] 단어

#CHECKLIST: 리스트 중복 제거 words = list(set(words))

# 문제
# 알파벳 소문자로 이루어진 N개의 단어가 들어오면 아래와 같은 조건에 따라 정렬하는 프로그램을 작성하시오.

# 길이가 짧은 것부터
# 길이가 같으면 사전 순으로
# 단, 중복된 단어는 하나만 남기고 제거해야 한다.

# 입력
# 첫째 줄에 단어의 개수 N이 주어진다. (1 ≤ N ≤ 20,000) 둘째 줄부터 N개의 줄에 걸쳐 알파벳 소문자로 이루어진 단어가 한 줄에 하나씩 주어진다. 주어지는 문자열의 길이는 50을 넘지 않는다.

# 출력
# 조건에 따라 정렬하여 단어들을 출력한다.

#[ ] Code i wrote
# 입력 받아 단어 리스트에 저장하기
N = int(input())
words = []
final_words=[]
len_w = []

for i in range(N):
    word = input()
    words.append(word)
    len_w.append(len(word))
    
# 단어 길이 리스트 만들기 (오름차순으로 정렬 됨), 단어 리스트 중복 제거
words = list(set(words))
len_w = list(set(len_w))

# 1. 짧은 길이 순서대로 같이 길이 단어끼리 temp에 모은 후 
for i in len_w:
    temp =[]
    for word in words:
        if int(i) == len(word):
            temp.append(word)
# 2. temp를 사전 형식으로 정렬. 순서대로 추가
    temp.sort()
    for i in temp:
        final_words.append(i)
    
# 최종 정렬 결과 출력
for i in final_words:
    print(str(i))
    
            



