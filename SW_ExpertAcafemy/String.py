# TODO: String, 패턴 매칭 알고리즘

# 패턴 매칭 : 본문에서 특정한 문자열 찾는 것 

# [ ] 고지식한 알고리즘 (Brute Forece) : O(M*N)
# 본문 문자열을 처음부터 끝까지 차례대로 순회하면서, 패턴 내의 문자들을 일일이 비교하는 방식

# [ ] KMP 알고리즘 : O(M+N)
# 불일치가 발생한 텍스트 문자열의 앞 부분에 어떤 문자가 있는지를 미리 알고 있으므로,
# 불일치가 발생한 앞 부분에 대하여 다시 비교하지 않고 매칭을 수행 

# [ ] 보이어-무어 알고리즘
# 오른 -> 왼으로 비교, 대부분의 상용 소프트웨어에서 채택하고 있는 알고리즘
# 패턴에 오른쪽 끝에 있는 문자가 불일치하고, 이 문자가 패턴 내에 존재하지 않는 경우, 이동거리는 패턴의 길이 만큼이 됨.

# [ ] 문자열 매칭 알고리즘 비교 : 찾고자 하는 문자열 패턴의 길이 m, 총 문자열 길이 n
# 고지식한 패턴 검색 알고리즘: 수행시간 O(mn)
# 카프-라빈 알고리즘 수: 수행시간 O(n)
# KMP 알고리즘: 수행시간 O(n)
# 보이어-무어 알고리즘: 수행시간 O(n)보다 적음

def exist_check(str1,str2,len_str1):
    try:
        index = str2.index(str1)
        return index
    except ValueError:
        return len_str1

N = int(input())

for i in range(1,N+1):
    str1 = input()
    str2 = input()

    n1 = len(str1)
    n2 = len(str2)
    start = 0

    while start+n1 < n2 :
        if str2[start] == str1[0]: #
            if str2[start:start+n1] == str1:
                print(f"#{i} 1")
                break
                
            start += 1
        else: 
            start += 1
        if start+n1 == n2: # 끝까지 비교하였지만, 문자열이 일치하지 않음
            print(f"#{i} 0")

'''
코드에 대해 검토해 보겠습니다.

코드의 주요 문제는 루프 조건에 있습니다. 주어진 코드에서는 두 문자열이 정확히 일치하는 경우에 대한 처리가 부족합니다. 또한, 루프를 끝내는 조건이 올바르지 않아서 문자열이 정확히 일치하지 않을 때 오류가 발생할 수 있습니다. 루프를 시작하는 인덱스를 올바르게 설정하여 모든 부분 문자열을 비교할 수 있도록 해야 합니다.

다음은 수정된 코드입니다.

python
Copy code
N = int(input())

for i in range(1, N+1):
    str1 = input()
    str2 = input()

    n1 = len(str1)
    n2 = len(str2)
    found = False

    for start in range(n2 - n1 + 1):  # 시작 인덱스를 올바르게 설정
        if str2[start:start+n1] == str1:
            print(f"#{i} 1")
            found = True
            break

    if not found:
        print(f"#{i} 0")
이 코드에서는 두 문자열이 정확히 일치하는 경우를 포함하여 모든 경우를 검사합니다. 문자열이 발견되면 해당 위치를 출력하고, 발견되지 않으면 0을 출력합니다.

'''