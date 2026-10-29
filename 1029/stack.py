# index       0     1     2     3     4
# stack = [None, None, None, None, None]
# top = -1

# Stack 초기화 함수
def init_stack(size):
    global stack, top
    stack = [None] * size
    top = -1


# Stack에 데이터 삽입 함수
def push(data):
    global top
    if is_full():
        return print("Stack이 가득 찼습니다.")
    else:
        top += 1
        stack[top] = data
        return print(f"현재 top: {top}")


# Stack에서 데이터 삭제 함수
def pop():
    global top
    if is_empty():
        return print("Stack이 비어있습니다.")
    else:
        data = stack[top]
        stack[top] = None
        top -= 1
        return print(f"pop된 데이터 : {data}, 현재 top: {top}")


# Stack의 최상단 데이터 확인 함수
def peek():
    if is_empty():
        print("Stack이 비어있습니다! peek 불가!")
        return None
    else:
        return stack[top]


# Stack Full 여부 확인 함수
def is_full():
    if top == len(stack) - 1:
        return True
    else:
        return False


# Stack Empty 여부 확인 함수
def is_empty():
    if top == -1:
        return True
    else:
        return False

init_stack(5)


# Stack 출력 함수
def print_stack(stack):
    print("----- 스택 상태 -----")
    # range(start, end, step) : start부터 end까지 step 만큼 증가/감소
    for i in range(len(stack)-1, -1, -1):
        print(stack[i])


push("커피")
push("녹차")
push("꿀물")
push("레몬차")
push("콜라")
print(f"peek() : {peek()}")
push("환타")
push("게토레이")

print_stack(stack)

for i in range(6):
    pop()

peek()

print_stack(stack)
