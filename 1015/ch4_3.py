class Node:
    def __init__(self, data):
        self.data = data
        self.link = None


class CircularLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        """리스트의 마지막에 노드를 추가한다."""
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            new_node.link = self.head
            return

        current = self.head
        while current.link != self.head:
            current = current.link

        current.link = new_node
        new_node.link = self.head

    def print_list(self):
        """헤드부터 한 바퀴만 순회하며 데이터를 출력한다."""
        if self.head is None:
            print("리스트가 비어 있습니다.")
            return

        current = self.head
        while True:
            print(current.data, end=" ")
            current = current.link
            if current == self.head:
                break
        print()


if __name__ == "__main__":
    circular_list = CircularLinkedList()

    for data in ["다현", "정연", "쯔위", "사나"]:
        circular_list.append(data)

    circular_list.print_list()