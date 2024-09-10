# myString = "oxooxoxxox"
# print(myString.split(''))
# answer = myString.split('x')
# answer= list(map(len,answer))

# NOTE: 파이썬에서 join() 함수는 반복 가능한(iterable) 요소들을 하나의 문자열로 연결(concatenate)하는 데 사용됩니다. 이는 split() 메서드의 반대 역할을 합니다.

# join()의 기본 구문은 다음과 같습니다:

# python
# Copy code
# 문자열.join(반복 가능한 객체)
# 여기서 문자열은 각 요소 사이에 삽입하려는 구분자(separator)이며, 반복 가능한 객체는 연결하려는 요소의 시퀀스입니다.

# 예를 들어:

# python
# Copy code
# my_list = ['사과', '바나나', '오렌지']
# result = '-'.join(my_list)
# print(result)
# 결과:

# Copy code
# 사과-바나나-오렌지
# 이 예제에서는 join()을 문자열 '-'에 대해 호출하고 있으므로, 결과 문자열에서 각 요소는 대시(-)로 구분됩니다.

# 구분자로 빈 문자열 ''을 사용하면 요소들이 구분자 없이 연결됩니다:

# python
# Copy code
# my_list = ['사과', '바나나', '오렌지']
# result = ''.join(my_list)
# print(result)
# 결과:

# Copy code
# 사과바나나오렌지
# join()은 리스트, 튜플 또는 문자열을 생성하는 제너레이터 표현식과 같은 문자열을 포함하는 모든 반복 가능한 객체와 함께 사용할 수 있습니다. 파이썬에서 문자열을 효율적으로 연결하는 편리한 방법입니다.
