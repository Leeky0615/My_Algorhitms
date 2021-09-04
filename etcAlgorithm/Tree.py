'''
    트리는 가계도와 같은 계층적인 구조를 표현할 때 사용할 수 있는 자료구조이다.
    루트 노드(root node) : 부모가 없는 최상위 노드
    단말 노드(leaf node) : 자식이 없는 노드
    크기(size) : 트리에 포함된 모든 노드의 개수
    깊이(depth) : 루트 노드부터의 거리
    높이(height) : 깊이 중 최댓값
    차수(degree) : 각 노드의 (자식 방향) 간선 개수
    기본적으로 트리의 크기가 N일 때, 전체 간선의 개수는 N-1개입니다.

    이진 탐색 트리
    이진 탐색이 동작할 수 있도록 고안된 효율적인 탐색이 가능한 자료구조의 일종
    이진 탐색 트리의 특징 : 왼쪽 자식 노드 < 부모 노드 < 오른쪽 자식 노드
     - 부모 노드보다 왼쪽 자식 노드가 작습니다
     - 부모 노드보다 오른쪽 자식 노드가 큽니다.

     트리의 순회
     트리 자료구조에 포함된 노드를 특정한 방법으로 한 번씩 방문하는 방법이다.
      - 트리의 정보를 시각적으로 확인할 수 있다
     전위 순회(pre-order traverse) : 루트를 먼저 방문합니다.
     중위 순회(in-order traverse) : 왼쪽 자식을 방문한 뒤에 루트를 방문합니다.
     후휘 순회(post-order traverse) : 오른쪽 자식을 방문한 뒤에 루트를 방문합니다.
'''

class Node:
    def __init__(self, data, left_node, right_node):
        self.data = data
        self.left_node = left_node
        self.right_node = right_node


# 전위 순회(Preorder Traversal)
def pre_order(node):
    print(node.data, end=' ')
    if node.left_node != None:
        pre_order(tree[node.left_node])
    if node.right_node != None:
        pre_order(tree[node.right_node])


# 중위 순회(Inorder Traversal)
def in_order(node):
    if node.left_node != None:
        in_order(tree[node.left_node])
    print(node.data, end=' ')
    if node.right_node != None:
        in_order(tree[node.right_node])


# 후위 순회(Postorder Traversal)
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
    tree[data] = Node(data, left_node, right_node)

pre_order(tree['A'])
print()
in_order(tree['A'])
print()
post_order(tree['A'])
'''
입력 예시
7
A B C
B D E
C F G
D None None
E None None
F None None
G None None
'''