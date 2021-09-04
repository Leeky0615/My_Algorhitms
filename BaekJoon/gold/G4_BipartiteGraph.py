'''
문제
그래프의 정점의 집합을 둘로 분할하여, 각 집합에 속한 정점끼리는 서로 인접하지 않도록 분할할 수 있을 때,
그러한 그래프를 특별히 이분 그래프 (Bipartite Graph) 라 부른다.

그래프가 입력으로 주어졌을 때, 이 그래프가 이분 그래프인지 아닌지 판별하는 프로그램을 작성하시오.

입력
입력은 여러 개의 테스트 케이스로 구성되어 있는데, 첫째 줄에 테스트 케이스의 개수 K(2≤K≤5)가 주어진다.
각 테스트 케이스의 첫째 줄에는 그래프의 정점의 개수 V(1≤V≤20,000)와 간선의 개수 E(1≤E≤200,000)가
빈 칸을 사이에 두고 순서대로 주어진다. 각 정점에는 1부터 V까지 차례로 번호가 붙어 있다.
이어서 둘째 줄부터 E개의 줄에 걸쳐 간선에 대한 정보가 주어지는데, 각 줄에 인접한 두 정점의 번호가 빈 칸을 사이에 두고 주어진다.

출력
K개의 줄에 걸쳐 입력으로 주어진 그래프가 이분 그래프이면 YES, 아니면 NO를 순서대로 출력한다.

예제 입력 1
2
3 2
1 3
2 3
4 4
1 2
2 3
3 4
4 2
예제 출력 1
YES
NO
'''

def bfs(x):
    queue = deque([x])
    bipartiteState[x] = 1
    while queue:
        value = queue.popleft()
        for i in graph[value]:
            if bipartiteState[i] == 0:
                bipartiteState[i] = -1 * bipartiteState[value]
                queue.append(i)
            elif bipartiteState[i] == bipartiteState[value]:
                return False
    return True


from collections import deque

t = int(input())  # 테스트케이스 개수
for _ in range(t):
    v, e = map(int, input().split())  # 정점(V) , 간선(e)
    graph = [[] for _ in range(v + 1)]  # 정점+1 만큼 만듬 -> 첫번째 값 사용X
    bipartiteState = [0] * (v + 1)  # 이분상태 배열 -> graph와 마찬가지로 첫번째 값 사용X
    flag = False  # 이분그래프 가능 결과 Flag

    for _ in range(e):  # 간선 수 만큼 반복해서 graph 채우기
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    for i in range(1, v+1):  # 첫번째 인덱스 사용X -> 1~V 까지만 사용
        if bipartiteState[i] == 0:  # 만약 이분그래프 상태 배열 값이 0이라면 -> 아직 BFS 수행이 안되었다면
            flag = bfs(i)  # bfs 수행
            if not flag:  # flag가 Flase라면 중지
                break

    print("YES" if flag else "NO")
