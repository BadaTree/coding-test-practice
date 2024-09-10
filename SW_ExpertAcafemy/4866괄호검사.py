#TODO: 4866. [파이썬 S/W 문제해결 기본] 4일차 - 괄호검사

'''

주어진 입력에서 괄호 {}, ()가 제대로 짝을 이뤘는지 검사하는 프로그램을 만드시오.
 

예를 들어 {( )}는 제대로 된 짝이지만, {( })는 제대로 된 짝이 아니다. 입력은 한 줄의 파이썬 코드일수도 있고, 괄호만 주어질 수도 있다.
 

정상적으로 짝을 이룬 경우 1, 그렇지 않으면 0을 출력한다.
 

print(‘{‘) 같은 경우는 입력으로 주어지지 않으므로 고려하지 않아도 된다.


 

[입력]


첫 줄에 테스트 케이스 개수 T가 주어진다.  1≤T≤50
 

다음 줄부터 테스트 케이스 별로 온전한 형태이거나 괄호만 남긴 한 줄의 코드가 주어진다.

 

[출력]
 

각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.

'''

# 체크 포인트 : 1. 괄호의 수가 짝수인가 , 2. 괄호 순서가 규칙적인가?

T = int(input()) # 테스트 수 입력
check_list = ["{","}","(",")"]


for i in range(1,T+1): # 테스트 수만큼 함수 반복
    result = True
    tempStr = input()
    tempStr = [j for j in tempStr if j in check_list] # 체크하는 괄호라면 남기고, 아니면 제외
   
    # 괄호의 수가 맞는지 체크 : tempStr.count('{') == tempStr.count('}')
    # 괄호 순서가 맞는지 체크 : (tempStr.index('{') % 2) != (tempStr.index('}') % 2)
    if '{' in tempStr or '}' in tempStr :
        if (tempStr.count('{') != tempStr.count('}')) or ((tempStr.index('{') % 2) == (tempStr.index('}') % 2)):
            result = False
      
    
    if '(' in tempStr or ')' in tempStr :
        if (tempStr.count('(') != tempStr.count(')')) or ((tempStr.index('(') % 2) == (tempStr.index(')') % 2)):
            result = False
      
    print(f"#{i} {int(result)}")
    
    
    
    '''
    T = int(input())  # 테스트 케이스 개수 입력
check_list = ["{", "}", "(", ")"]

for i in range(1, T + 1):  # 각 테스트 케이스에 대해 반복
    tempStr = input()
    stack = []  # 괄호를 저장할 스택
    result = 1  # 결과 변수 초기화

    for char in tempStr:
        if char in check_list:
            if char == "{" or char == "(":
                stack.append(char)  # 여는 괄호는 스택에 push
            else:  # 닫는 괄호일 때
                if not stack:  # 스택이 비어있는 경우
                    result = 0  # 올바르지 않은 괄호 쌍
                    break
                else:
                    top = stack.pop()  # 스택에서 꺼내기
                    if (char == "}" and top != "{") or (char == ")" and top != "("):
                        result = 0  # 괄호 쌍이 일치하지 않음
                        break

    if stack:  # 스택에 남아있는 괄호가 있는 경우
        result = 0  # 올바르지 않은 괄호 쌍

    print(f"#{i} {result}")

    '''