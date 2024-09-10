# TODO : 24.05.29 코테 스터디 

# [ ] 포켓몬 

import collections

def solution(nums):
    return min(len(collections.Counter(nums)), (len(nums) /2))

# [ ] 전화번호 목록 

def solution(phone_book):
    phone_book.sort() # ['119','119234','34567']
    
    for i in range(len(phone_book) - 1):
        if phone_book[i + 1].startswith(phone_book[i]): 
            return False
    return True

# [ ] 베스트앨범

def sortedplays(indexs, plays):
    result = []
    for i in indexs:
        if len(result) == 0:
            result.insert(0, i)
        elif plays[i] >= plays[result[0]]:  # 첫 배열일 때
            result.insert(0, i)
        else:
            result.append(i)
    return result 

def solution(genres, plays):
    sortedGenres = {}
    FinalResult = []
    
    # Genres 재생 횟수 계산
    for i in range(len(genres)):
        if genres[i] not in sortedGenres:
            sortedGenres[genres[i]] = [plays[i], [i]]
        else:
            sortedGenres[genres[i]][0] += plays[i]
            sortedGenres[genres[i]][1].append(i)
            
    # 많이 재생된 순서대로 내림차순 정렬
    sortedGenres = dict(sorted(sortedGenres.items(), key=lambda item: item[1][0], reverse=True))
    
    for key, value in sortedGenres.items():
        indices = value[1]
        sorted_indices = sorted(indices, key=lambda x: plays[x], reverse=True)
        FinalResult.extend(sorted_indices[:2])
    
    return FinalResult

# 예제 입력
genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]

# 결과 출력
result = solution(genres, plays)
print(result)

# [ ] 완주하지 못한 선수 

def solution(participant, completion):
    answer = ''
    temp = 0
    dic = {}
    for part in participant:
        dic[hash(part)] = part
        temp += int(hash(part))
    for com in completion:
        temp -= hash(com)
    answer = dic[temp]

    return answer



# TODO : Hash Table 구현하기

'''

파이썬에서 해시 테이블(Hash Table)을 구현하는 방법은 여러 가지가 있지만, 가장 간단한 방법은 파이썬의 내장 데이터 구조인 딕셔너리(dict)를 사용하는 것입니다. 그러나 교육 목적으로, 기본적인 해시 테이블을 직접 구현해보겠습니다. 이 예제에서는 충돌 해결을 위해 체이닝(Chaining) 기법을 사용할 것입니다.

해시 테이블 구현
해시 함수: 주어진 키를 해시 값으로 변환하는 함수.
체이닝을 위한 버킷: 동일한 해시 값을 가진 키-값 쌍들을 저장하기 위한 리스트.
삽입, 검색, 삭제 메서드: 해시 테이블의 기본 연산.
구현 코드
python
코드 복사
class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]
    
    def hash_function(self, key):
        return hash(key) % self.size
    
    def insert(self, key, value):
        index = self.hash_function(key)
        for kvp in self.table[index]:
            if kvp[0] == key:
                kvp[1] = value
                return
        self.table[index].append([key, value])
    
    def search(self, key):
        index = self.hash_function(key)
        for kvp in self.table[index]:
            if kvp[0] == key:
                return kvp[1]
        return None
    
    def delete(self, key):
        index = self.hash_function(key)
        for i, kvp in enumerate(self.table[index]):
            if kvp[0] == key:
                del self.table[index][i]
                return True
        return False
    
    def __repr__(self):
        return str(self.table)

# 해시 테이블 사용 예제
ht = HashTable()
ht.insert("apple", 1)
ht.insert("banana", 2)
ht.insert("grape", 3)
ht.insert("apple", 10)  # "apple" 키의 값을 업데이트

print("Search 'apple':", ht.search("apple"))  # 10
print("Search 'banana':", ht.search("banana"))  # 2
print("Search 'grape':", ht.search("grape"))  # 3
print("Search 'orange':", ht.search("orange"))  # None

print("Delete 'banana':", ht.delete("banana"))  # True
print("Delete 'orange':", ht.delete("orange"))  # False

print(ht)  # 해시 테이블의 현재 상태 출력
설명
생성자 (__init__):

size: 해시 테이블의 크기(버킷의 수).
table: 빈 리스트를 크기만큼 만들어 초기화합니다.
해시 함수 (hash_function):

파이썬의 내장 hash 함수를 사용하여 키를 해시 값으로 변환하고, 이를 테이블 크기로 나눈 나머지를 사용합니다.
삽입 메서드 (insert):

키와 값을 해시 테이블에 삽입합니다.
동일한 키가 이미 존재하면 값을 업데이트합니다.
검색 메서드 (search):

주어진 키에 해당하는 값을 검색하여 반환합니다.
키가 존재하지 않으면 None을 반환합니다.
삭제 메서드 (delete):

주어진 키에 해당하는 값을 삭제합니다.
삭제에 성공하면 True, 실패하면 False를 반환합니다.
출력 (__repr__):

해시 테이블의 현재 상태를 문자열로 반환합니다.
이 구현은 기본적인 해시 테이블의 동작을 이해하는 데 도움이 됩니다. 실용적인 애플리케이션에서는 파이썬의 dict를 사용하는 것이 더 효율적이고 편리합니다.

번역된 내용

파이썬에서 해시 테이블(Hash Table)을 구현하는 방법은 여러 가지가 있지만, 가장 간단한 방법은 파이썬의 내장 데이터 구조인 딕셔너리(dict)를 사용하는 것입니다. 그러나 교육 목적으로, 기본적인 해시 테이블을 직접 구현해보겠습니다. 이 예제에서는 충돌 해결을 위해 체이닝(Chaining) 기법을 사용할 것입니다.

해시 테이블 구현

해시 함수: 주어진 키를 해시 값으로 변환하는 함수.

체이닝을 위한 버킷: 동일한 해시 값을 가진 키-값 쌍들을 저장하기 위한 리스트.

삽입, 검색, 삭제 메서드: 해시 테이블의 기본 연산.

구현 코드
python
코드 복사
class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]
    
    def hash_function(self, key):
        return hash(key) % self.size
    
    def insert(self, key, value):
        index = self.hash_function(key)
        for kvp in self.table[index]:
            if kvp[0] == key:
                kvp[1] = value
                return
        self.table[index].append([key, value])
    
    def search(self, key):
        index = self.hash_function(key)
        for kvp in self.table[index]:
            if kvp[0] == key:
                return kvp[1]
        return None
    
    def delete(self, key):
        index = self.hash_function(key)
        for i, kvp in enumerate(self.table[index]):
            if kvp[0] == key:
                del self.table[index][i]
                return True
        return False
    
    def __repr__(self):
        return str(self.table)

# 해시 테이블 사용 예제
ht = HashTable()
ht.insert("apple", 1)
ht.insert("banana", 2)
ht.insert("grape", 3)
ht.insert("apple", 10)  # "apple" 키의 값을 업데이트

print("Search 'apple':", ht.search("apple"))  # 10
print("Search 'banana':", ht.search("banana"))  # 2
print("Search 'grape':", ht.search("grape"))  # 3
print("Search 'orange':", ht.search("orange"))  # None

print("Delete 'banana':", ht.delete("banana"))  # True
print("Delete 'orange':", ht.delete("orange"))  # False

print(ht)  # 해시 테이블의 현재 상태 출력
설명

생성자 (__init__):



size: 해시 테이블의 크기(버킷의 수).

table: 빈 리스트를 크기만큼 만들어 초기화합니다.



해시 함수 (hash_function):



파이썬의 내장 hash 함수를 사용하여 키를 해시 값으로 변환하고, 이를 테이블 크기로 나눈 나머지를 사용합니다.



삽입 메서드 (insert):



키와 값을 해시 테이블에 삽입합니다.

동일한 키가 이미 존재하면 값을 업데이트합니다.



검색 메서드 (search):



주어진 키에 해당하는 값을 검색하여 반환합니다.

키가 존재하지 않으면 None을 반환합니다.



삭제 메서드 (delete):



주어진 키에 해당하는 값을 삭제합니다.

삭제에 성공하면 True, 실패하면 False를 반환합니다.



출력 (__repr__):



해시 테이블의 현재 상태를 문자열로 반환합니다.



이 구현은 기본적인 해시 테이블의 동작을 이해하는 데 도움이 됩니다. 실용적인 애플리케이션에서는 파이썬의 dict를 사용하는 것이 더 효율적이고 편리합니다.
'''