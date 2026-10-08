# 202630127 장민준
## 9월10일(2주차)
### 마크다운 문법

# h1 태그
## h2 태그
### h3 태그
.....
###### h6태그

**볼드**

***이텔릭+볼드***

~~취소선~~

<u>밑줄</u>

1. 감자
2. 옥수수
3. 배추

* 감자
* 옥수수
* 배추
    * 배추 김치
        * 신 김치

### 코드 블럭

```py
print("Hello World!")
```

### 링크
[구글 바로가기](https://google.com "구글 사이트")

[코드 블럭](#코드-블럭 "코드블럭 예제")

![깃 로고](./git.png "git logo")

---

# 202630127 장민준
## 9월17일(3주차)
### 리스트의 삽입과 삭제

- 리스트의 인덱스를 이용해 원하는 위치의 데이터에 접근하기
- `append()`로 리스트의 마지막에 데이터 추가하기
- 빈 공간에 새 데이터를 넣고, 뒤의 데이터를 한 칸씩 이동해 삽입하기
- 데이터를 한 칸씩 이동해 원하는 항목을 삭제하기
- 임시 변수와 인덱스를 이용해 리스트 요소의 순서 바꾸기

```py
kakao = ["가나", "다라", "마바", "사아", "자차"]
kakao.append("삽입")

temp = kakao[4]
kakao[4] = kakao[5]
kakao[5] = temp
```

## 10월1일(4주차)
### 리스트 기본 조작

- 빈 리스트를 생성하고 `len()`으로 리스트의 길이 확인하기
- `append()`를 사용해 데이터를 차례대로 추가하기
- `for`문과 인덱스를 이용해 리스트 전체를 순회하며 출력하기

```py
kakao = []
kakao.append("다현")
kakao.append("정연")

for i in range(len(kakao)):
    print(kakao[i], end=", ")
```

### 연결 리스트

- `Node` 클래스로 데이터와 다음 노드를 가리키는 링크 만들기
- 여러 노드를 `link`로 연결해 연결 리스트 구성하기
- 현재 노드를 다음 노드로 이동하며 연결 리스트 순회하기
- 새 노드를 기존 노드 사이에 삽입하기
- 링크를 다시 연결해 삽입된 노드를 건너뛰고 원래 구조로 복구하기

```py
class Node:
    def __init__(self):
        self.data = None
        self.link = None
```

## 10월8일(5주차)
### 연결 리스트 함수화와 검색

`1001/ch4_1.py`에서는 노드를 직접 생성하고 `link`를 하나씩 연결해 연결 리스트를 만들었다.
`1008/ch4_1_2.py`에서는 이 과정을 함수와 반복문으로 확장해 더 유연하게 관리할 수 있도록 했다.

- `print_nodes()` 함수로 연결 리스트 전체를 순회하며 출력하기
- `find_data()` 함수로 원하는 데이터를 가진 노드 검색하기
- 검색 결과가 있으면 해당 노드를 반환하고, 없으면 빈 노드로 처리하기
- `insert_node()` 함수로 특정 데이터 앞에 새 노드 삽입하기
- 첫 번째 노드 앞, 중간, 마지막 위치에 노드를 삽입하는 경우를 나누어 처리하기
- `memory`에 생성된 노드를 저장하고 `head`로 첫 번째 노드 관리하기
- 삽입 함수가 호출될 때마다 `current`와 `pre`를 초기화해 이전 탐색 상태가 남지 않도록 하기

### `ch4_1.py`와 `ch4_1_2.py`의 차이

| 구분 | `1001/ch4_1.py` | `1008/ch4_1_2.py` |
|---|---|---|
| 노드 생성 | 노드를 직접 생성하고 연결 | 반복문으로 여러 노드 생성 |
| 출력 | 노드에 직접 접근하거나 반복문 사용 | `print_nodes()` 함수로 출력 |
| 검색 | 검색 기능 없음 | `find_data()` 함수로 데이터 검색 |
| 삽입 | 코드 블록에서 한 번만 직접 처리 | `insert_node()` 함수로 반복 사용 |
| 관리 방식 | `node1`, `node2`와 같은 변수로 관리 | `head`, `current`, `pre`, `memory`로 관리 |

```py
def find_data(find_data):
    current = head
    if current.data == find_data:
        return current

    while current.link is not None:
        current = current.link
        if current.data == find_data:
            return current

    return Node()

search_node = find_data("쯔위")
print(search_node.data)
```

### 실행 예제

```py
insert_node("다현", "재남")
print_nodes(head)

search_node = find_data("쯔위")
print("검색 결과:", search_node.data)
```
