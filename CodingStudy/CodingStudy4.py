# TODO : 2024.06.01 코테스터디 해쉬 관련 자유 문제 


# [ ] 의상 (Level2, 프로그래머스)
# https://school.programmers.co.kr/learn/courses/30/lessons/42578 


# [ ] 메뉴 리뉴얼 (level2, 프로그래머스)
# https://school.programmers.co.kr/learn/courses/30/lessons/72411

# [ ] 패션왕 신해빈 (실버 3, 백준)
# https://www.acmicpc.net/problem/9375


# TODO: Hash 관련 추천 문제를 풀어보자 


# [ ] 완주하지 못한 선수 

def solution(participant, completion):
    answer = ''
    temp = 0
    dic = {}
    for part in participant:
        dic[hash(part)] = part
        temp += int(hash(part))
    for com in completion:
        temp -= hash(com)
    answer = dic[temp]

    return answer


# [ ]나는야 포켓몬 마스터 이다솜
# https://www.acmicpc.net/problem/1620

import sys

input = sys.stdin.read
data = input().split()

N = int(data[0])
M = int(data[1])

pocket_num = {}
pocket_name = {}

# 포켓몬 정보 받아 도감에 저장하기
index = 2
for i in range(1, N + 1):
    name = data[index]
    pocket_num[str(i)] = name
    pocket_name[name] = i
    index += 1

# 포켓몬 맞추기 : 숫자 -> 이름, 이름 -> 숫자
for i in range(M):
    info = data[index]
    index += 1
    # 포켓몬 번호가 들어왔을 때
    if info.isdigit():
        print(pocket_num.get(info))
    # 포켓몬 이름 들어올 때
    else:
        print(pocket_name.get(info))



# [ ] 듣보잡
# https://www.acmicpc.net/problem/1764

import sys

input = sys.stdin.read
data = input().split()

N = int(data[0])
M = int(data[1])

# 인덱스나 순서가 필요 없음 ! 공통인만 찾으면 되니까 set으로 구현
# 듣도 못한 사람 set으로 저장 
not_heard = set()
index = 2
for _ in range(N):
    not_heard.add(data[index])
    index += 1
    
# 보도 못한 사람 set으로 저장
not_seen = set()
for _ in range(M):
    not_seen.add(data[index])
    index += 1

# 듣도 보도 못한 사람을 교집합으로 찾기
result = sorted(not_heard & not_seen)

# Print the results
print(len(result))
for name in result:
    print(name)

# [ ] 신고 결과 받기
# https://school.programmers.co.kr/learn/courses/30/lessons/92334

# [ ] 순위 검색
# https://school.programmers.co.kr/learn/courses/30/lessons/72412