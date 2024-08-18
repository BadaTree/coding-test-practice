
# Q.6045 정수 3개를 입력받아 합과 평균을 출력해보자.
a,b,c = input().split()
sum = int(a)+ int(b) + int(c)
avg = sum / 3
print(sum,format(avg,".2f"))

# Q.6046 정수 1개를 입력받아 2배 곱해 출력해보자.
num = input()
print(int(num)*2)
# Q.6047 정수 2개(a, b)를 입력받아 a를 2b배 곱한 값으로 출력해보자.
a,b = input().split()
print(int(a)<<int(b))

# Q.6048 두 정수(a, b)를 입력받아 a가 b보다 작으면 True 를, a가 b보다 크거나 같으면 False 를 출력하는 프로그램을 작성해보자.
a,b = input().split()
if int(a) < int(b) :
    print(True)
else: print(False)

# Q.6049 두 정수(a, b)를 입력받아 a와 b의 값이 같으면 True 를, 같지 않으면 False 를 출력하는 프로그램을 작성해보자.
a,b = input().split()
if int(a) == int(b) :
    print(True)
else: print(False)

# Q.6050 두 정수(a, b)를 입력받아 b의 값이 a의 값 보다 크거나 같으면 True 를, 같지 않으면 False 를 출력하는 프로그램을 작성해보자.
a,b = input().split()
if int(a) <= int(b) :
    print(True)
else: print(False)

# Q.6051 두 정수(a, b)를 입력받아 a의 값이 b의 값과 서로 다르면 True 를, 같으면 False 를 출력하는 프로그램을 작성해보자.
a,b = input().split()
if int(a) != int(b) :
    print(True)
else: print(False)

# Q.6052 정수가 입력되었을 때, True/False 로 평가해주는 프로그램을 작성해보자.
n = int(input())
if n == 0 :
    print(bool(n))
else: print(True)

# Q.6053 정수값이 입력될 때, 그 불 값을 반대로 출력하는 프로그램을 작성해보자.
n = int(input())
if n == 0 :
    print(not bool(n))
else: print(False)

# Q.6054 2개의 정수값이 입력될 때, 그 불 값이 모두 True 일 때에만 True 를 출력하는 프로그램을 작성해보자.
a,b = input().split()
a = bool(int(a))
b = bool(int(b))
if a and b :
    print(True)
else: print(False)

# Q.6055 2개의 정수값이 입력될 때,그 불 값이 하나라도 True 일 때에만 True 를 출력하는 프로그램을 작성해보자.
a,b = input().split()
a = bool(int(a))
b = bool(int(b))
if a or b :
    print(True)
else: print(False)

# Q.6056 2개의 정수값이 입력될 때, 그 불 값(True/False) 이 서로 다를 때에만 True 를 출력하는 프로그램을 작성해보자.
a,b = input().split()
a = bool(int(a))
b = bool(int(b))
if a != b :
    print(True)
else: print(False)

# Q.6057 2개의 정수값이 입력될 때, 그 불 값(True/False) 이 서로 같을 때에만 True 를 출력하는 프로그램을 작성해보자.
a,b = input().split()
a = bool(int(a))
b = bool(int(b))
if a == b :
    print(True)
else: print(False)

# Q.6058 2개의 정수값이 입력될 때, 그 불 값(True/False) 이 서로 같을 때에만 True 를 출력하는 프로그램을 작성해보자.
a,b = input().split()
a = bool(int(a))
b = bool(int(b))
if (not a) and (not b) :
    print(True)
else: print(False)

# Q.6059 입력 된 정수를 비트단위로 참/거짓을 바꾼 후 정수로 출력해보자.비트단위(bitwise)연산자 ~ 를 붙이면 된다.(~ : tilde, 틸드라고 읽는다.)
num = input()
print(~int(num))

# Q.6060 입력된 정수 두 개를 비트단위로 and 연산한 후 그 결과를 정수로 출력해보자.비트단위(bitwise)연산자 &를 사용하면 된다.(and, ampersand, 앰퍼센드라고 읽는다.)
a,b = input().split()
print(int(a)&int(b))

# Q.6061 입력된 정수 두 개를 비트단위로 or 연산한 후 그 결과를 정수로 출력해보자.비트단위(bitwise) 연산자 |(or, vertical bar, 버티컬바)를 사용하면 된다.
a,b = input().split()
print(int(a)|int(b))

# Q.6062 입력된 정수 두 개를 비트단위로 xor 연산한 후 그 결과를 정수로 출력해보자.비트단위(bitwise) 연산자 |(or, vertical bar, 버티컬바)를 사용하면 된다.
a,b = input().split()
print(int(a)^int(b))

# Q.6063 입력된 두 정수(a, b) 중 큰 값을 출력하는 프로그램을 작성해보자. 단, 3항 연산을 사용한다.
a,b = input().split()
a = int(a)
b = int(b)
result = a if (a>=b) else b
print(result)

# Q.6064 입력된 세 정수 a, b, c 중 가장 작은 값을 출력하는 프로그램을 작성해보자. 단, 3항 연산을 사용한다.
a,b,c = input().split()
a = int(a)
b = int(b)
c = int(c)
result = (b if (a >= b) else a) if ((b if (a >= b) else a) <= c) else c
print(result)

# Q.6065 3개의 정수(a, b, c)가 입력되었을 때, 짝수만 출력해보자.
a,b,c = input().split()
a = int(a)
b = int(b)
c = int(c)

if a % 2 == 0 :
    print(a)
if b % 2 == 0 :
    print(b)
if c % 2 == 0 :
    print(c)

# Q.6066 3개의 정수(a, b, c)가 입력되었을 때, 짝(even)/홀(odd)을 출력해보자.
a,b,c = input().split()
a = int(a)
b = int(b)
c = int(c)

if a % 2 == 0 :
    print("even")
else:
    print("odd")
if b % 2 == 0 :
    print("even")
else:
    print("odd")
if c % 2 == 0 :
    print("even")
else:
    print("odd")

# Q.6067 0이 아닌 정수 1개가 입력되었을 때, 음(-)/양(+)과 짝(even)/홀(odd)을 구분해 분류해보자.
# 음수이면서 짝수이면, A
# 음수이면서 홀수이면, B
# 양수이면서 짝수이면, C
# 양수이면서 홀수이면, D
# 를 출력한다.

rnd = int(input())
if rnd != 0 :
    if rnd < 0:
        if rnd % 2 == 0:
            print("A")
        else:
            print("B")
    else:
        if rnd % 2 == 0:
            print("C")
        else:
            print("D")

# Q.6068 점수(정수, 0 ~ 100)를 입력받아 평가를 출력해보자.
score = int(input())
if  90 <= score <= 100:
    print("A")
elif 70 <= score <= 89:
    print("B")
elif 40 <= score <= 69:
    print("C")
else : print("D")

# Q.6069 평가를 문자(A, B, C, D, ...)로 입력받아 내용을 다르게 출력해보자.
score = input()
if score == "A": print("best!!!")
elif score == "B": print("good!!")
elif score == "C": print("run!")
elif score == "D": print("slowly~")
else:print("what?")

# Q.6070 월이 입력될 때 계절 이름이 출력되도록 해보자.
#
# 월 : 계절 이름
# 12, 1, 2 : winter
#   3, 4, 5 : spring
#   6, 7, 8 : summer
#   9, 10, 11 : fall

mon = int(input())
if mon == 12 or mon == 1 or mon == 2:
    print("winter")
elif mon == 3 or mon == 4 or mon == 5:
    print("spring")
elif mon == 6 or mon == 7 or mon == 8:
    print("summer")
elif mon == 9 or mon == 10 or mon == 11:
    print("fall")

# Q.6071 임의의 정수가 줄을 바꿔 계속 입력된다.0이 아니면 입력된 정수를 출력하고, 0이 입력되면 출력을 중단해보자.
while True:
    num = int(input())
    if num == 0:
        break
    else:
        print(num)