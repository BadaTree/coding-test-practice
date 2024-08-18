# TODO : 나중에 풀어야하는 문제 리스트

'''
[ 5. 18 (토) 스터디 문제 공유 ]

 
회전하는 큐: https://st-lab.tistory.com/216

 
요세푸스: https://www.acmicpc.net/problem/1158

 
암기왕: https://www.acmicpc.net/problem/2776

 
좋은단어: https://www.acmicpc.net/problem/3986

 
뒤집기: https://www.acmicpc.net/problem/1439

 
단어뒤집기2: https://www.acmicpc.net/problem/17413

기능 개발 : https://school.programmers.co.kr/learn/courses/30/lessons/42586

[ 5. 25 (토) 스터디 문제 공유 ]

제로: https://www.acmicpc.net/problem/10773

도키도키 간식드리미: https://www.acmicpc.net/problem/12789

최소직사각형: https://school.programmers.co.kr/learn/courses/30/lessons/86491

막대기: https://www.acmicpc.net/problem/17608

프린터 큐: https://www.acmicpc.net/problem/1966

더 맵게: https://school.programmers.co.kr/learn/courses/30/lessons/42626

달팽이: https://www.acmicpc.net/problem/1913

level2문제: https://school.programmers.co.kr/learn/courses/30/lessons/147354
level3문제: https://school.programmers.co.kr/learn/courses/30/lessons/42579

폰켓몬(level1): https://school.programmers.co.kr/learn/courses/30/lessons/1845
전화번호 목록(level2): https://school.programmers.co.kr/learn/courses/30/lessons/42577


# [ ] 메뉴 리뉴얼 (level2, 프로그래머스)
# https://school.programmers.co.kr/learn/courses/30/lessons/72411


# [ ] 패션왕 신해빈 (실버 3, 백준)
# https://www.acmicpc.net/problem/9375

# [ ] 미로 탈출 명령어 
# https://school.programmers.co.kr/learn/courses/30/lessons/150365


# [ ] 순위 검색 (Level2, 프로그래머스)
# https://school.programmers.co.kr/learn/courses/30/lessons/72412


상근이의 여행: https://www.acmicpc.net/problem/9372 

무한이진트리: https://www.acmicpc.net/problem/2078

Smallest Number in infinite Set: https://leetcode.com/problems/smallest-number-in-infinite-set/description

카펫: https://school.programmers.co.kr/learn/courses/30/lessons/42842
'''

# [ ] 백준 2231

def find_smallest_constructor(target):
    # 각 자리수의 합이 최대 9이므로 탐색 시작점을 target - 9 * len(str(target))로 설정
    start = max(1, target - 9 * len(str(target)))
    
    for candidate in range(start, target):
        sum_with_digits = candidate + sum(map(int, str(candidate)))
        if sum_with_digits == target:
            return candidate
    return 0

# 입력 처리
target = int(input())

# 결과 출력
print(find_smallest_constructor(target))

'''
4. 생성자 
𝑀
M의 최소값 추정
생성자 
𝑀
M은 
𝑁
N보다 작거나 같은 자연수입니다. 
𝑀
M을 최대한 작게 만들기 위해 
𝑀
M의 각 자리수 합을 최대값으로 생각해 봅니다. 이는 
𝑁
N에서 최대 자리수 합을 뺀 값입니다.

예시로 설명
𝑁
=
216
N=216을 예로 들어 보겠습니다.

자리수 합 계산:

216
216은 3자리 수입니다.
각 자리수가 최대일 때 자리수 합은 
9
+
9
+
9
=
27
9+9+9=27입니다.
생성자 
𝑀
M의 최소값:

216
216에서 각 자리수 합의 최대값을 뺀 값을 계산합니다.
216
−
27
=
189
216−27=189
이 계산은 가능한 생성자 
𝑀
M의 최소값을 추정하기 위한 방법입니다. 실제로 189보다 작은 값은 216의 생성자가 될 수 없습니다. 이는 
𝑀
M이 너무 작아져서 각 자리수 합을 더해도 
𝑁
N에 도달하지 못하기 때문입니다.

요약
분해합의 정의: 
𝑁
=
𝑀
+
(
M의 각 자리수 합
)
N=M+(M의 각 자리수 합)
자리수 합의 최대값: 각 자리수가 최대일 때의 합
생성자 최소값 추정: 
𝑁
−
(
자리수 합의 최대값
)
N−(자리수 합의 최대값)
'''