# 노드의 데이터와 다음 노드 연결을 초기화
class Node:
    def __init__(self):
        self.data = None
        self.link = None

# 생성자에 데이터를 직접 전달하는 방식은 사용할 수 없음
# node1 = Node("다현")

# 다섯 개의 노드를 생성하고 순서대로 연결
node1 = Node()
node1.data = "다현"

node2 = Node()
node2.data = "정연"
node1.link = node2

node3 = Node()
node3.data = "쯔위"
node2.link = node3

node4 = Node()
node4.data = "사나"
node3.link = node4

node5 = Node()
node5.data = "지효"
node4.link = node5

# 각 노드에 직접 접근해 데이터 출력
print(node1.data, end=", ")
print(node1.link.data, end=", ")
print(node1.link.link.data, end=", ")
print(node1.link.link.link.data, end=", ")
print(node1.link.link.link.link.data)

# 연결 리스트를 순회하며 데이터 출력
print('\n\n연결리스트 출력')
current = node1
while current.link is not None:
    current = current.link
    print(current.data, end=", ")

# 두 번째 노드와 세 번째 노드 사이에 새 노드 삽입
new_node = Node()
new_node.data = "재남"
new_node.link = node3
node2.link = new_node

# 새 노드가 삽입된 연결 리스트 출력
print('\n\n연결리스트 출력')
current = node1
while current.link is not None:
    current = current.link
    print(current.data, end=", ")

# 새 노드를 건너뛰도록 연결해 삽입 작업 취소
node2.link = node3

# 원상복구된 연결 리스트 출력
print('\n\n연결리스트 출력')
current = node1
while current.link is not None:
    current = current.link
    print(current.data, end=", ")
