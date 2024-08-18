# TODO : 2024.06.05 코테스터디 해쉬 관련 자유 문제 


# [ ] 신고 결과 받기 (Level1, 프로그래머스)
# https://school.programmers.co.kr/learn/courses/30/lessons/92334

def solution(id_list, report, k):
    # 신고 당한 id : 해당 id를 신고한 id 인덱스 배열을 저장한 딕셔너리 생성
    id_dic = {} # 각 id의 인덱스를 저장한 딕셔너리
    del_id = []
    result = [0]*len(id_list)

    # {id:index}
    for i in range(len(id_list)) :
        id_dic[f"{id_list[i]}"] = list(str(i)) 
    
    for i in range(len(report)):
        a, b = report[i].split(' ')
        
        # 한 유저가 같은 유저를 여러번 신고시 1회로 처리. 중복 제거
        if id_dic[f"{a}"][0] not in id_dic[f"{b}"][1:]: 
            id_dic[f"{b}"].append(id_dic[f"{a}"][0])
            
    # 각 id마다 k 이상인지 check
    # 즉 정지된 id만 남기고 다 제외 
    for i,j in id_dic.items():
        if len(j)-1 >= k : 
            del_id.append(i)
    for i in del_id:
        for j in range(1,len(id_dic[f"{i}"])):
            id_index = id_dic[f"{i}"][j]
            result[int(id_index)] += 1
            
    # 최종 id마다 받은 메일 수를 반환하는 배열 출력 
    return result


# [ ] 순위 검색 (Level2, 프로그래머스)
# https://school.programmers.co.kr/learn/courses/30/lessons/72412


# [ ] 의상 (Level2, 프로그래머스)
# https://school.programmers.co.kr/learn/courses/30/lessons/42578 

#[의상의 이름, 의상의 종류], 각 종류별로 최대 1가지 의상, 하루에 최소 한 개의 의상

def solution(clothes):
    clothes_dic ={}
    # 종류 별로 의상 정리 
    for clothe in clothes:
        clothes_dic[clothe[1]] = clothes_dic.get(clothe[1],0) + 1
            
    # 의상을 아예 안 입은 경우 +1 해주고 총 조합의 수 카운트
    result = 1
    for type in clothes_dic:
        result *= (clothes_dic[type]+1)
    
    return result-1

# [ ] 메뉴 리뉴얼 (level2, 프로그래머스)
# https://school.programmers.co.kr/learn/courses/30/lessons/72411


# [ ] 패션왕 신해빈 (실버 3, 백준)
# https://www.acmicpc.net/problem/9375

# [ ] 미로 탈출 명령어 
# https://school.programmers.co.kr/learn/courses/30/lessons/150365



