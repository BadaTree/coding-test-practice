
# Q.6007 "C:\Download\'hello'.py" 출력하기
print("\"C:\\Download\\\'hello\'.py\"")
# -> 문자열에 특수 기호가 들어갈 때는 맨 끝이 아니라 중간에도 특수기호 앞에 \를 붙여준다.


# Q.6008 print("Hello\nWorld") 출력하기
print("print(\"Hello\\nWorld\")")

# Q.6009 변수에 문자 1개를 저장한 후 변수에 저장되어 있는 문자를 그대로 출력해보자.
what = input()
print(what)

# Q.6010 변수에 정수값을 저장한 후 정수로 변환하여 출력해보자.
int_var = input()
print(int(int_var))

# Q.6011 변수에 실수 값을 저장한 후 실수로 변환하여 출력해보자.
int_var = input()
print(float(int_var))

# Q.6012 줄을 바꿔 정수(integer) 2개를 입력받아 줄을 바꿔 출력해보자.
one = input()
two = input()
print(int(one))
print(int(two))

# Q.6013 줄을 바꿔 문자(character) 2개를 입력받고, 순서를 바꿔 한 줄씩 출력해보자.
one = input()
two = input()
print(two)
print(one)

# Q.6014 실수 1개 입력받아 3번 출력하기
one = input()
print(float(one))
print(float(one))
print(float(one))

# Q.6015 공백을 두고 입력된정수(integer) 2개를 입력받아 줄을 바꿔 출력해보자.
one,two = input().split()
print(one)
print(two)

# Q.6016 공백을 두고 문자(character) 2개를 입력받아 순서를 바꿔 출력해보자.
one,two = input().split()
print(two,one)

# Q.6017 정수(integer), 실수, 문자(character), 문자열(string) 등 1개만 입력받아 한 줄로 3번 출력해보자.
one = input()
print(one,one,one)

# Q.6018 24시간 시:분 형식으로 시간이 입력될 때, 그대로 출력하는 연습을 해보자.
hour,min = input().split(':')
print(hour,min,sep= ":")

# Q.6019 "연도.월.일"을 입력받아 "일-월-연도" 순서로 바꿔 출력해보자.
y,m,d = input().split('.')
print(d,m,y,sep='-')

# Q.6020 왼쪽 6자리는 생년월일(YYMMDD)이고, 오른쪽 7자리는 성별,출생지역,확인코드로 구성되어있다.
# 주민번호를 입력받아 형태를 바꿔 출력해보자.
num_front,num_back = input().split('-')
print(num_front+num_back)

# Q.6021 알파벳과 숫자로 이루어진 단어 1개가 입력된다. 입력받은 단어의 각 문자를 한 줄에 한 문자씩 분리해 출력한다.
voca = input()
for i in range(5):
    print(voca[i])

# Q.6022 6자리의 연월일(YYMMDD)을 입력받아 나누어 출력해보자.
yymmdd = input()
print(yymmdd[0:2],yymmdd[2:4],yymmdd[4:6])

# Q.6023 시:분:초 형식으로 시간이 입력될 때 분만 출력해보자. 어떻게 분만 출력해야 할지 주의 깊게 생각해야한다.
h,m,s = input().split(':')
print(m)

# Q.6024 알파벳 문자와 숫자로 이루어진 단어 2개를 입력받아 순서대로 붙여 출력하는 프로그램을 작성해보자.
w1,w2  = input().split()
print(w1+w2)

# Q.6025 정수 2개를 입력받아 합을 출력하는 프로그램을 작성해보자.
a,b = input().split()
sum = int(a)+int(b)
print(sum)

# Q.6026 실수 2개를 입력받아 합을 출력하는 프로그램을 작성해보자.
a = input()
b = input()
sum = float(a)+float(b)
print(sum)

# Q.6027 10진수를 입력받아 16진수(hexadecimal)로 출력해보자.
hex_num = input()
print('%x'%int(hex_num))

# Q.6028 10진수를 입력받아 16진수(hexadecimal) 대문자로 출력해보자.
hex_num = input()
print('%X'%int(hex_num))

# Q.6029 10진수를 입력받아 8진수(octal)로 출력해보자.
octal_num = input()
print('%o'%int(octal_num,16))

# Q.6030 영문자 1개를 입력받아 10진수 유니코드(Unicode) 값으로 출력해보자.
n = ord(input())
print(n)

# Q.6031 10진 정수 1개를 입력받아 유니코드 문자로 출력해보자.
c = int(input())
print(chr(c))

# Q.6032 입력된 정수의 부호를 바꿔 출력해보자.
pos_num = input()
print(-int(pos_num))

# Q.6033 문자 1개를 입력받아 그 다음 문자를 출력해보자.
# 영문자 'A'의 다음 문자는 'B'이고, 숫자 '0'의 다음 문자는 '1'이다.
uni_num = ord(input())
print(chr(uni_num+1))

# Q.6034 정수 2개(a, b)를 입력받아 a에서 b를 뺀 차를 출력하는 프로그램을 작성해보자.
a,b = input().split()
print(int(a)-int(b))

# Q.6035 실수 2개(f1, f2)를 입력받아 곱을 출력하는 프로그램을 작성해보자.
a,b = input().split()
print(float(a)*float(b))

# Q.6036 단어와 반복 횟수를 입력받아 여러 번 출력해보자.
word,n = input().split()
print(word*int(n))

# Q.6037 반복 횟수와 문장을 입력 받아 여러번 출력해보자
n = input()
word = input()
print(word*int(n))

# Q.6038 정수 2개(a, b)를 입력받아 a를 b번 곱한 거듭제곱을 출력하는 프로그램을 작성해보자.
a,b = input().split()
print(int(a)**int(b))

# Q.6039 실수 2개(a, b)를 입력받아 a를 b번 곱한 거듭제곱을 출력하는 프로그램을 작성해보자.
a,b = input().split()
print(float(a)**float(b))

# Q.6040 정수 2개(a, b) 를 입력받아 a를 b로 나눈 몫을 출력해보자.
a,b = input().split()
print(int(a)//int(b))

# Q.6041 정수 2개(a, b) 를 입력받아 a를 b로 나눈 나머지를 출력해보자.
a,b = input().split()
print(int(a)%int(b))

# Q.6042 실수 1개를 입력받아 소숫점 이하 두 번째 자리까지의 정확도로 반올림한 값을 출력해보자.
a = float(input())
print(format(a,".2f"))

# Q.6043 실수 2개(f1, f2)를 입력받아 f1 을 f2 로 나눈 값을 출력해보자.
# 이 때 소숫점 넷째자리에서 반올림하여 무조건 소숫점 셋째 자리까지 출력한다.
a,b = input().split()
result = float(a)/float(b)
print(format(result,".3f"))

# Q.6044 정수 2개(a, b)를 입력받아 합, 차, 곱, 몫, 나머지, 나눈 값을 자동으로 계산해보자.
# 단, b는 0이 아니다.
a,b = input().split()
print(int(a)+int(b))
print(int(a)-int(b))
print(int(a)*int(b))
print(int(a)//int(b))
print(int(a)%int(b))
print(format(int(a)/int(b),".2f"))

