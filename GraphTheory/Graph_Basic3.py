'''
    신장 트리
    그래프에서 모든 노드를 포함하면서 사이클이 존재하지 않는 부분 그래프
      - 모든 노드가 포함되어 서로 연결되면서 사이클이 존재하지 않는다는 조건은
        트리의 조건이기도 합니다.
    최소 신장 트리
    최소한의 비용으로 구성되는 신장 트리를 찾아야 할 때 어떻게 해야할까요?
    예를 들어 N개의 ㅗㄷ시가 존재하는 사오항에서 두 도시 사이에 도로를 놓아
    전체 도시가 서로 연결될 수 있게 도로를 설치하는 경우를 생각해봅시다.
      - 두 도시 A,B를 선택했을 때 A에서 B로 이동하는 경로가 반드시 존재하도록
        도로를 설치합니다.
    크루스칼 알고리즘
     - 대표적인 최소 신장 트리 알고리즘이다.
     - 그리디 알고리즘으로 분류된다.
     - 구체적인 동작 과정은 다음과 같다
       1. 간선 데이터를 비용에 따라 오름차순으로 정렬한다
       2. 간선을 하나씩 확인하며 현재의 간선이 사이클을 발생시키는지 확인한다.
          1) 사이클이 발생하지 않는 경우 최소 신장 트리에 포함시킨다.
          2) 사이클이 발생하는 경우 최소 신장 트리에 포함시키지 않는다.
       3. 모든 간선에 대하여 2번의 과정을 반복한다.
     - 간선의 개수가 E개 일 때, O(ElogE)의 시간 복잡도를 가진다.
     - 크루스칼 알고리즘에서 가장 많은 시간을 요구하는 곳은 간선을 정렬하는 부분이다.
     

입력 예시
7 9
1 2 29
1 5 75
2 3 35
2 6 34
3 4 7
4 6 23
4 7 13
5 6 53
6 7 25
출력 예시
159
'''


# 특정 원소가 속한 집합을 찾기
def find_parent(parent, x):
    # 루트 노드를 찾을 때까지 재귀 호출
    if parent[x] != x:
        return find_parent(parent, parent[x])
    return parent[x]


# 두 원소가 속한 집합을 찾기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


# 노드의 개수와 간선(union 연산)의 개수 입력 받기
v, e = map(int, input().split())

parent = [0] * (v + 1)  # 부모 테이블 초기화 하기

# 모든 간선을 담을 리스트와, 최종 비용을 담을 변수
edges = []
result = 0

# 부모 테이블 상에서, 부모를 자기 자신으로 초기화
for i in range(1, v + 1):
    parent[i] = i

# 모든 간선에 대한 정보를 입력 받기
for _ in range(e):
    a, b, cost = map(int, input().split())
    # 비용순으로 정렬하기 위해서 튜플의 첫 번째 원소를 비용으로 설정
    edges.append((cost, a, b))

# 간선을 비용순으로 정렬
edges.sort()

# 간선을 하나씩 확인하며
for edge in edges:
    cost, a, b = edge
    # 사이클이 발생하지 않는 경우에만 집합에 포함
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost

print('v :', v)
print('e :', e)
print('edges :', edges)
print(parent)
print(result)
