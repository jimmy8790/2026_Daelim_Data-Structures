class Queue:
    """고정된 크기의 원형 큐를 구현한다."""

    def __init__(self, size):
        if size < 1:
            raise ValueError("큐의 크기는 1 이상이어야 합니다.")

        self.size = size
        self.queue = [None] * size
        self.front = 0
        self.rear = 0

    def is_empty(self):
        """큐가 비어 있으면 True를 반환한다."""
        return self.front == self.rear

    def is_full(self):
        """큐가 가득 차 있으면 True를 반환한다."""
        return (self.rear + 1) % self.size == self.front

    def enqueue(self, data):
        """큐의 뒤에 데이터를 삽입한다."""
        if self.is_full():
            print("큐가 꽉 찼습니다.")
            return False

        self.rear = (self.rear + 1) % self.size
        self.queue[self.rear] = data
        return True

    def dequeue(self):
        """큐의 앞에서 데이터를 추출한다."""
        if self.is_empty():
            print("큐가 비었습니다.")
            return None

        self.front = (self.front + 1) % self.size
        data = self.queue[self.front]
        self.queue[self.front] = None
        return data

    def peek(self):
        """추출하지 않고 다음 데이터를 확인한다."""
        if self.is_empty():
            print("큐가 비었습니다.")
            return None

        return self.queue[(self.front + 1) % self.size]

    def print_queue(self):
        """큐의 현재 상태와 front, rear 위치를 출력한다."""
        print("큐 상태:", self.queue)
        print("front:", self.front, "rear:", self.rear)


if __name__ == "__main__":
    queue = Queue(5)

    for data in ["화사", "솔라", "문별", "휘인"]:
        queue.enqueue(data)
    queue.print_queue()

    print("다음에 추출될 데이터:", queue.peek())
    print("추출된 데이터:", queue.dequeue())
    print("추출된 데이터:", queue.dequeue())

    # 앞쪽 공간을 비운 뒤에도 원형으로 다시 사용할 수 있다.
    queue.enqueue("선미")
    queue.enqueue("재남")
    queue.print_queue()

    while not queue.is_empty():
        print("추출된 데이터:", queue.dequeue())

    queue.dequeue()