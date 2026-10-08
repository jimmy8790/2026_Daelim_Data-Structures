class Node:
    # 노드의 데이터와 다음 노드 연결을 초기화
    def __init__(self):
        self.data = None
        self.link = None

# 연결 리스트의 노드들을 순서대로 출력
def print_nodes(start):
    current = start
    if current.link is None:
        return
    print(current.data, end=' ')
    while current.link is not None:
        current = current.link
        print(current.data, end=' ')
    print()

def find_data(find_data):
    global memory, head, current, pre
    current = head
    if current.data == find_data:
        return current
    while current.link is not None:
        current = current.link
        if current.data == find_data:
            return current
    return Node()  # 빈 노드 반환

# 연결 리스트에 노드를 삽입하는 함수
def insert_node(find_data, insert_data):
    global memory, head, current, pre
    current = head
    pre = None

    # 첫 번째 노드 삽입
    if find_data == head.data:
        node = Node()
        node.data = insert_data
        node.link = head
        head = node
        memory.append(node)
        return

    while current.link is not None:
        pre = current
        current = current.link
        if current.data == find_data:
            node = Node()
            node.data = insert_data
            node.link = current
            pre.link = node
            memory.append(node)
            return

    # 마지막 노드 삽입
    node = Node()
    node.data = insert_data
    current.link = node
    memory.append(node)

# 연결 리스트 생성에 사용할 전역 변수와 데이터
memory = []
head, current, pre = None, None, None
dataArray = ["다현", "정연", "쯔위", "사나", "지효"]

# 파일을 직접 실행할 때 연결 리스트 생성
if __name__ == "__main__":
    node = Node()
    node.data = dataArray[0]
    head = node
    memory.append(node)

    # 나머지 데이터로 노드를 생성하고 앞 노드와 연결
    for data in dataArray[1:]:
        pre = node
        node = Node()
        node.data = data
        pre.link = node
        memory.append(node)
        
    insert_node("다현", "재남")  # 다현 앞에 재남 삽입
    print_nodes(head)

    insert_node("사나", "솔라")  # 사나 앞에 솔라 삽입
    print_nodes(head)

    insert_node("재남", "문별")  # 지효 뒤에 문별 삽입
    print_nodes(head)  # 연결 리스트 출력

    # 연결 리스트에서 특정 데이터를 검색
    search_node = find_data("쯔위")
    print("검색 결과:", search_node.data)

    # 존재하지 않는 데이터 검색
    search_node = find_data("다현이")
    if search_node.data is None:
        print("검색 결과: 데이터를 찾을 수 없습니다.")