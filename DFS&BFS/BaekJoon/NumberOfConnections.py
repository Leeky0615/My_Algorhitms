'''
문제
방향 없는 그래프가 주어졌을 때, 연결 요소 (Connected Component)의 개수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 정점의 개수 N과 간선의 개수 M이 주어진다. (1 ≤ N ≤ 1,000, 0 ≤ M ≤ N×(N-1)/2)
둘째 줄부터 M개의 줄에 간선의 양 끝점 u와 v가 주어진다. (1 ≤ u, v ≤ N, u ≠ v)
같은 간선은 한 번만 주어진다.

출력
첫째 줄에 연결 요소의 개수를 출력한다.

예제 입력 1
6 5
1 2
2 5
5 1
3 4
4 6
예제 출력 1
2
예제 입력 2
6 8
1 2
2 5
5 1
3 4
4 6
5 4
2 4
2 3
'''


# dfs함수 선언
def dfs(x):
    visited[x] = True  # 정점 x를 방문 처리한다.
    for i in graph[x]:  # 정점 x와 연결된 모든 정점 확인
        if not visited[i]:  # 방문하지 않았다면,
            dfs(i)  # 해당 정점을 다시 탐색한다.


n, m = map(int, input().split())  # 정점의 수(n), 간선의 수(m)를 입력
arr = [list(map(int, input().split())) for _ in range(m)]  # 간선의 양끝점 정보 입력
graph = [[] for _ in range(n + 1)]  # 그래프 리스트 초기화
visited = [False] * (n + 1)  # 방문 기록 리스트 초기화
count = 0  # 연결 요소 개수 초기화

# 양끝점 정보를 graph 리스트(2차원)로 바꿈
for i in arr:
    graph[i[0]].append(i[1])
    graph[i[1]].append(i[0])

# 정점의 개수 만큼 반복
for i in range(1, n + 1):
    if not visited[i]:  # 방문하지 않았다면
        dfs(i)  # dfs 수행
        count += 1  # 연결 요소 개수 추가

print(count)  # 연결 요소 개수 출력
