class Node:
    def __init__(self):  # 노드가 생성될 때 실행되는 초기화 함수
        self.data = None  # 노드에 저장할 데이터를 준비
        self.link = None  # 다음 노드를 가리킬 연결을 준비

# node1 = Node("다현")  # 생성자에 데이터를 전달하는 방식은 현재 사용할 수 없음
node1 = Node()  # 첫 번째 노드 생성
node1.data = "다현"  # 첫 번째 노드에 데이터 저장

node2 = Node()  # 두 번째 노드 생성
node2.data = "정연"  # 두 번째 노드에 데이터 저장
node1.link = node2  # 첫 번째 노드가 두 번째 노드를 가리키도록 연결

node3 = Node()  # 세 번째 노드 생성
node3.data = "쯔위"  # 세 번째 노드에 데이터 저장
node2.link = node3  # 두 번째 노드와 세 번째 노드를 연결

node4 = Node()  # 네 번째 노드 생성
node4.data = "사나"  # 네 번째 노드에 데이터 저장
node3.link = node4  # 세 번째 노드와 네 번째 노드를 연결

node5 = Node()  # 다섯 번째 노드 생성
node5.data = "지효"  # 다섯 번째 노드에 데이터 저장
node4.link = node5  # 네 번째 노드와 다섯 번째 노드를 연결

print(node1.data, end=", ")  # 첫 번째 노드의 데이터 출력
print(node1.link.data, end=", ")  # 두 번째 노드의 데이터 출력
print(node1.link.link.data, end=", ")  # 세 번째 노드의 데이터 출력
print(node1.link.link.link.data, end=", ")  # 네 번째 노드의 데이터 출력
print(node1.link.link.link.link.data)  # 다섯 번째 노드의 데이터 출력

print('\n\n연결리스트 출력')  # 연결 리스트 순회 결과를 표시
current = node1  # 순회를 시작할 현재 노드를 첫 번째 노드로 설정
while current.link is not None:  # 다음 노드가 있으면 반복
    current = current.link  # 현재 노드를 다음 노드로 이동
    print(current.data, end=", ")  # 이동한 노드의 데이터 출력



new_node = Node()  # 중간에 삽입할 새 노드 생성
new_node.data = "재남"  # 새 노드에 데이터 저장
new_node.link = node3  # 새 노드가 기존 세 번째 노드를 가리키도록 연결
node2.link = new_node  # 두 번째 노드가 새 노드를 가리키도록 변경

print('\n\n연결리스트 출력')  # 새 노드가 삽입된 연결 리스트 출력
current = node1  # 다시 첫 번째 노드부터 순회 시작
while current.link is not None:  # 다음 노드가 있으면 반복
    current = current.link  # 다음 노드로 이동
    print(current.data, end=", ")  # 현재 노드의 데이터 출력



node2.link = node3  # 새 노드를 건너뛰고 두 번째 노드를 세 번째 노드에 다시 연결

print('\n\n연결리스트 출력')  # 원상복구된 연결 리스트 출력
current = node1  # 첫 번째 노드부터 다시 순회 시작
while current.link is not None:  # 다음 노드가 있으면 반복
    current = current.link  # 다음 노드로 이동
    print(current.data, end=", ")  # 현재 노드의 데이터 출력