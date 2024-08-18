# [ ] Tree 개념 
# https://blog.naver.com/zzzxxx3166/223533254579
# [나동빈 트리 핵심 요약 & 구현](https://www.youtube.com/watch?v=i5yHkP1jQmo)
# [이진트리의 구현 및 순회 알고리즘]


# [ ] 트리의 순회 구현하기
'''
class Node:
    def __init__(self,data,left_node,right_node):
        self.data = data
        self.left_node = left_node
        self.right_node = right_node
        
# 전위 순회(Preorder Traversal) 부모 -> 왼쪽자식 -> 오른자식
def pre_order(node):
    print(node.data,end=' ')
    if node.left_node != None :
        pre_order(tree[node.left_node])
    if node.right_node != None:
        pre_order(tree[node.right_node])
        
# 중위 순회(Inorder Traversal) 왼쪽자식 -> 부모 -> 오른자식
def in_order(node):
    if node.left_node != None:
        in_order(tree[node.left_node])
    print(node.data,end=' ')
    if node.right_node !=None:
        in_order(tree[node.right_node])

# 후위 순회(Postorder Traversal) 왼쪽자식 ->  오른자식 부모 ->
def post_order(node):
    if node.left_node != None:
        post_order(tree[node.left_node])
    if node.right_node != None:
        post_order(tree[node.right_node])
    print(node.data, end=' ')
    
n = int(input())
tree = {}

for i in range(n):
    data, left_node, right_node = input().split()
    if left_node == "None":
        left_node = None
    if right_node == "None":
        right_node = None
    tree[data] = Node(data,left_node,right_node)

'''
'''
# 트리구조를 저장한 Tree 딕셔너리의 모습 
{
    1: Node(1, 2, 3),
    2: Node(2, 4, 5),
    3: Node(3, None, None),
    4: Node(4, None, None),
    5: Node(5, None, None)
}
'''
'''
    
pre_order(tree['A'])
print()
in_order(tree['A'])
print()
post_order(tree['A'])

'''
# [ ] 실습
# Node 클래스 생성
class Node:
    def __init__(self,data, left_node,right_node):
        self.data = data
        self.left_node = left_node
        self.right_node = right_node
        

def pre_order(node):
    print(node.data,end=' ')
    if node.left_node != None:
        pre_order(tree[node.left_node])
    if node.left_node != None:
        pre_order(tree[node.right_node])

def in_order(node):
    if node.left_node != None :
        in_order(tree[node.left_node])
    print(node.data, end =' ')
    if node.right_node != None:
        in_order(tree[node.right_node])
        
def post_order(node):
    if node.left_node != None:
        post_order(tree[node.left_node])
    if node.right_node :
        post_order(tree[node.right_node])
    print(node.data,end=' ')
    
N = int(input())
tree = {}
# 노드들의 객체를 생성하고, 노드가 이어진 트리를 딕셔너리로 구현 
for i in range(N):
    value,left_node, right_node = input().split(' ')
    if left_node == 'None':
        left_node = None
    if right_node == 'None':
        right_node = None
    tree[value] = Node(value,left_node,right_node)
    
pre_order(tree['A']) # 시작은 항상 루프 노드에서    
print()
in_order(tree['A'])
print()
post_order(tree['A'])


# [ ] Class 기본 개념 및 생성 해보기
# https://blog.naver.com/zzzxxx3166/223538539678

# Q. 'Student' 클래스를 생성하여, name, age, student_id, courses 속성을 저장하고, 아래 메서드를 정의.
# 'enroll': courses을 등록하는 메서드, 'list_courses' : self.courses를 출력하는 메서드, 
# 'introduce': f"Hello, my name is {self.name}, I am {self.age} years old and my student ID is {self.student_id}."를 출력하는 메서드

'''
class student:
    # 생성자 메서드
    def __init__(self, name, age,student_id):
        self.name = name # 속성
        self.age = age # 속성
        self.student_id = student_id # 속성
        self.course = []# 속성
        
    # 메서드들
    def eroll(self,course):
        self.course.append(course)
        print(f"{self.name} has enrolled in {course}")

    def list_courses(self):
        return self.course
    
    def introduce(self):
        return f"Hello, my name is {self.name}, I am {self.age} years old and my student ID is {self.student_id}."
    
# 객체 생성
alice = student("alice", 15, 1729)
tom = student("tom", 16,134)

# 수업 등록 
alice.eroll("History 101")
tom.eroll("math 201")

# 수업 리스트 출력
print(alice.list_courses())
print(tom.list_courses())

# 자기소개 
print(alice.introduce())
print(tom.introduce())

'''

# [ ] 이진 탐색 트리 클래스 구현

class Node:
    def __init__(self, key): # 클래스 생성자 함수 ( 속성은 부모노드, 왼쪽 자식, 오른쪽 자식 )
        self.key = key
        self.left = None
        self.right = None
        
class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    # 삽입 메서드
    def insert(self, key):
        if self.root is None: # 첫 노드일 때, 루트에 아무 노드가 없을 때
            self.root = Node(key)
        else:
            self._insert(self.root, key) # 루트에 다른 노드가 있을 때

    # 이진 탐색 트리 조건에 맞게 맞는 위치에 노드를 추가하기 위한 함수 
    # current_node.key: root에 저장되어 있는 노드 값, key : 현재 추가하려는 노드의 값
    def _insert(self, current_node, key):
        # 저장된 노드 값보다 작으면 왼쪽 자식노드로 이동
        if key < current_node.key:  
            if current_node.left is None: # 왼쪽 자식노드가 없다면 그 위치에 바로 추가 
                current_node.left = Node(key)
            else:
                self._insert(current_node.left, key) # 왼쪽 자식 노드가 있다면, 왼쪽 자식노드를 타고 level 하나 더 내려감
        # 저장된 노드 값보다 크다면 오른쪽 자식노드로 이동
        elif key > current_node.key:
            if current_node.right is None:
                current_node.right = Node(key) # 오른쪽 자식노드가 없다면 그대로 추가 
            else:
                self._insert(current_node.right, key)# 오른쪽 자식 노드가 있다면 오른쪽 자식 노드를 타고 한 level 더 내려감
    
    # 검색 메서드
    def search(self, key):
        return self._search(self.root, key)
    
    def _search(self, current_node, key):
        # 탐색할 노드가 더 이상 없거나 찾는 노드를 찾았을 때 !
        if current_node is None or current_node.key == key: 
            return current_node
        # 노드의 값이 현재 노드보다 작다면 왼쪽으로, 크다면 오른쪽으로 이동 
        if key < current_node.key: 
            return self._search(current_node.left, key)
        else:
            return self._search(current_node.right, key)
    
    # 최소값 찾기
    # 트리 노드의 최솟값은 리프노드의 왼쪽 노드임. 
    # 즉 가장 하위 레벨의 왼쪽 자식 노드를 찾는 함수 
    def find_min(self, current_node): 
        while current_node.left is not None:
            current_node = current_node.left
        return current_node
    
    # 삭제 메서드
    def delete(self, key):
        self.root = self._delete(self.root, key)
    
    def _delete(self, current_node, key):
        if current_node is None:
            return current_node
        
        if key < current_node.key:
            current_node.left = self._delete(current_node.left, key)
        elif key > current_node.key:
            current_node.right = self._delete(current_node.right, key)
        else:
            # Node with only one child or no child
            if current_node.left is None:
                return current_node.right
            elif current_node.right is None:
                return current_node.left
            
            # Node with two children: Get the inorder successor (smallest in the right subtree)
            temp = self.find_min(current_node.right)
            
            # Copy the inorder successor's content to this node
            current_node.key = temp.key
            
            # Delete the inorder successor
            current_node.right = self._delete(current_node.right, temp.key)
        
        return current_node
    
    # 중위 순회 (Inorder Traversal)
    def inorder(self):
        result = []
        self._inorder(self.root, result)
        return result
    
    def _inorder(self, current_node, result):
        if current_node:
            self._inorder(current_node.left, result)
            result.append(current_node.key)
            self._inorder(current_node.right, result)
# 이진 탐색 트리 생성
bst = BinarySearchTree()

# 삽입
bst.insert(10)
bst.insert(5)
bst.insert(20)
bst.insert(3)
bst.insert(7)
bst.insert(15)

# 검색
node = bst.search(7)
print(node.key if node else "Not found")  # 출력: 7

# 삭제
bst.delete(10)

# 중위 순회print(bst.inorder())  # 출력: [3, 5, 7, 15, 20]


# [ ] 이진 탐색 트리 구현 실습

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None
    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else :
            self._insert(self.root,key)
    def _insert (self,current_key,key):
        if key < current_key:
            if current_key.left is None :
                current_key.left = Node(key)
            else :
                self._insert(current_key.left, key)
        else:
            if current_key.right is None :
                current_key.right = Node(key)
            else: 
                self._insert(current_key.right,key)
    def search(self, key):
        return self._search(self.root, key)
    
    def _search(self, current_key, key):
        if current_key is None or current_key == key:
            return current_key
        else :                
            if key < current_key:
                self._search(current_key.left,key)
            else:
                self._search(current_key.right,key)
                
    def find_min(self,current_key):
        while current_key.left is not None:
            current_key = current_key.left
        return current_key
    
    
    
