# TREE에 대해 공부해 보자 

# [ ] 기본 개념 강의
# https://www.youtube.com/watch?v=ohrwGtqeW-I&t=9s
# https://youtu.be/i57ZGhOVPcI?si=lrDWF1wZA4pLekpc

# [ ] 예제 문제 풀이 

# 1. 트리 만들기 (백준 14244, 실4)
# https://www.acmicpc.net/problem/14244
n,m = map(int,input().split())

now_node=0
count = m-1
for i in range(1,n):
    if m==2: #  모든 노드가 일직선으로 연결
        print(now_node,i)
        now_node+=1
    else: # 가지를 추가하여 리프 노드의 수를 맞춥니다.
        print(now_node,i)
        now_node+=1
        if count:
            now_node-=1
            count-=1


# 2. 세모 (백준 27966, 실3)
# https://www.acmicpc.net/problem/27966

# 3. 상근이의 여행 (백준 9372, 실4)
# https://www.acmicpc.net/problem/9372

# 연결 그래프에서 최소 신장 트리(MST)를 찾는 문제
# 최신장 트리소  = 그래프에서 모든 노드(국가)를 연결하는 최소 간선(비행기의 수)의 집합
# NOTE: 최소 신장 트리의 특성상 N개의 노드를 연결하는 데 필요한 최소 간선 수는 N−1입니다. 
# 

import sys
input = sys.stdin.read

data = input().strip().split()

T = int(data[0])
index = 1

    
for _ in range(T):
    N = int(data[index]) # 국가의 수 (노드 수)
    M = int(data[index + 1]) # 비행기의 수 (간선 수)
    index += 2 +(M*2)
        
    # 모든 국가를 여행하기 위해 필요한 최소 비행기 수는 국가 수 - 1
    print(N-1)


# 4. Binary tree (백준 13237, 실3)
# https://www.acmicpc.net/problem/13237

# 5. 트리 순회 (백준 1991, 실1)
# https://www.acmicpc.net/problem/1991

# 6. @@ 트리의 부모 찾기 (백준11725)
# https://www.acmicpc.net/problem/11725

# 7. 무한 이진트리 (백준 2078, 실2)
# https://www.acmicpc.net/problem/2078

# 9. @@표현 가능한 이진트리 
# https://school.programmers.co.kr/learn/courses/30/lessons/150367