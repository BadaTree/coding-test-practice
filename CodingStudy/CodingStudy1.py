# 2024.05.22  Coding Test 문제 풀이 

# [ ] 1. 모의고사 

'''
문제 설명
수포자는 수학을 포기한 사람의 준말입니다. 수포자 삼인방은 모의고사에 수학 문제를 전부 찍으려 합니다. 수포자는 1번 문제부터 마지막 문제까지 다음과 같이 찍습니다.

1번 수포자가 찍는 방식: 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, ...
2번 수포자가 찍는 방식: 2, 1, 2, 3, 2, 4, 2, 5, 2, 1, 2, 3, 2, 4, 2, 5, ...
3번 수포자가 찍는 방식: 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, ...

1번 문제부터 마지막 문제까지의 정답이 순서대로 들은 배열 answers가 주어졌을 때, 가장 많은 문제를 맞힌 사람이 누구인지 배열에 담아 return 하도록 solution 함수를 작성해주세요.

제한 조건
시험은 최대 10,000 문제로 구성되어있습니다.
문제의 정답은 1, 2, 3, 4, 5중 하나입니다.
가장 높은 점수를 받은 사람이 여럿일 경우, return하는 값을 오름차순 정렬해주세요.
'''
# KeyPoint :  

def solution(answers):
    # 수포자들의 패턴
    ans1 = [1, 2, 3, 4, 5]
    ans2 = [2, 1, 2, 3, 2, 4, 2, 5]
    ans3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    # 각 수포자의 점수
    score_list = [0, 0, 0]

    # 채점
    for i in range(len(answers)):
        if answers[i] == ans1[i % len(ans1)]: # 수포자들의 정답지는 패턴이 반복됨을 활용
            score_list[0] += 1
        if answers[i] == ans2[i % len(ans2)]:
            score_list[1] += 1
        if answers[i] == ans3[i % len(ans3)]:
            score_list[2] += 1

    # 가장 높은 점수 찾기
    max_val = max(score_list)
    result = [i + 1 for i in range(3) if score_list[i] == max_val]

    return result


# [ ] 표 편집   1245566

'''
https://school.programmers.co.kr/learn/courses/30/lessons/81303

'''
def solution(n, k, cmds):
    ori_list = [i for i in range(n)]
    last_del = []
    result = ""
    
    # cmd 수행
    for cmd in cmds:
        if cmd[0] == "U":
            k -= int(cmd[2:])
            k = max(0, k)
        elif cmd[0] == "D":
            k += int(cmd[2:])
            k = min(len(ori_list) - 1, k)
        elif cmd[0] == "C":
            last_del.append((k, ori_list[k]))  # 삭제된 값과 인덱스 기록
            ori_list.pop(k)
            if k >= len(ori_list):
                k = len(ori_list) - 1
        elif cmd[0] == "Z":
            if last_del:
                index, value = last_del.pop()
                ori_list.insert(index, value)
                if index <= k:
                    k += 1
    
    # 순서 상관없이 존재하는지만 체크 
    for i in range(n):
        if i in ori_list:
            result += "O"
        else:
            result += "X"
    
    return result

