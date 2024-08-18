#TODO: 문자열 재정렬
# 알파벳 대문자와 숫자(0~9)로만 구성된 문자열이 입력으로 주어집니다.
# 이때 모드 알파벳을 오름차순으로 정렬하여 이어서 출력한 뒤에 모든 숫자를 더한 값을 이어서 출력합니다.
# 예: K1KA5A5CB7이라는 값이 들어오면 ABCKK13을 출력합니다.

#CHECKLIST:
#[x]: 알파벳인지 어떻게 확인하지?
# x.isalpha()를 이용하여 간편하게 체크
#[x]: 어떻게 리스트를 문자열로 변환하지?
# 변수 = ''.join(alpa) *'-'를 넣으면 a-l-p-h-a

#[ ] Code i wrote
input = input()
sum = 0
alpa = []

# input 문자열에서 숫자만 제거하고, 합 계산하기
for i in input:
    num = False
    for j in range(10):
        if i == str(j):
            sum += j
            num = True
    if not(num):  
        alpa.append(i)

# 알파벳만 남은 문자열 오름차순 정렬하기
alpa.sort()

# 오름차순 정렬 문자열과 숫자 합 이어 붙이기
string_alpa = ''.join(alpa)
print(string_alpa+str(sum))

#[ ]: Answer code
input = input()
sum = 0
alpha = []

# input 문자열에서 숫자만 제거하고, 합 계산하기
for i in input:
    if i.isalpha():
        alpha.append(i)
    else:
        sum += int(i)

# 알파벳만 남은 문자열 오름차순 정렬하기
alpha.sort()

# 오름차순 정렬 문자열과 숫자 합 이어 붙이기
if sum != 0:
    alpha.append(sum)
string_alpa = ''.join(alpha)
print(string_alpa+str(sum))