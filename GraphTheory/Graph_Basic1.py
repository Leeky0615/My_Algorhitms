'''
    서로소 집합
    - 공통 원소가 없는 두 집합을 의미합니다.
    - 서로소 부분 집합들로 나누어진 원소들의 데이터를 처리하기 위한 자료구조이다
    - 두 종류의 연산을 지원한다
      ㅇ 합집합 : 두 개의 원소가 포함된 집합을 하나의 집합으로 합치는 연산
      ㅇ 찾기 : 특정한 원소가 속한 집합이 어떤 집합인지 알려주는 연산
    - 서로소 집합 자료구조는 합치기 찾기 자료구조라고도 불린다.
    - 여러개의 합치기 연산이 주어졌을 때 서로소 집합 자료구조의 동작 과정
      ㅇ 합집합 연산을 확인하여, 서로 연결된 두 노드 A,B를 확인한다.
         A와 B의 루트 노드 A', B'를 각각 찾는다
         A'를 B'의 부모 노드로 설정한다
      ㅇ 모든 합집합 연산을 처리할 때까지 1번의 과정을 반복한다
    - 연결성을 통해 집합의 형태를 파악할 수 있다.
'''


# 특정 원소가 속한 집합을 찾기
def find_parent(parent, x):
    # 루트 노드를 찾을 때까지 재귀 호출
    if parent[x] != x:
        return find_parent(parent, parent[x])
    return x


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

# 부모 테이블상에서, 부모를 자기 자신으로 초기화
for i in range(1, v + 1):
    parent[i] = i

# union 연산을 각각 수행
for i in range(e):
    a, b = map(int, input().split())
    union_parent(parent, a, b)

# 각 원소가 속한 집합 출력하기
print('각 원소가 속한 집합 : ', end='')
for i in range(1, v+1):
    print(find_parent(parent,i), end=' ')

print()

# 부모 테이블 내용 출력하기
print('부모 테이블 : ', end='')
for i in range(1, v+1):
    print(parent[i], end=' ')


'''
    찾기 함수를 최적화 하기 위한 방법으로 경로 압축을 이용할 수 있다.
'''
# 특정 원소가 속한 집합을 찾기
def find_parent(parent, x):
    # 루트 노드를 찾을 때까지 재귀 호출
    if parent[x] != x:
        return find_parent(parent, parent[x])
    return parent[x]
