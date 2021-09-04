'''
N×M의 행렬로 표현되는 맵이 있다. 맵에서 0은 이동할 수 있는 곳을 나타내고, 1은 이동할 수 없는 벽이 있는 곳을 나타낸다.
당신은 (1, 1)에서 (N, M)의 위치까지 이동하려 하는데, 이때 최단 경로로 이동하려 한다.
최단경로는 맵에서 가장 적은 개수의 칸을 지나는 경로를 말하는데, 이때 시작하는 칸과 끝나는 칸도 포함해서 센다.
만약에 이동하는 도중에 한 개의 벽을 부수고 이동하는 것이 좀 더 경로가 짧아진다면, 벽을 한 개 까지 부수고 이동하여도 된다.
한 칸에서 이동할 수 있는 칸은 상하좌우로 인접한 칸이다.
맵이 주어졌을 때, 최단 경로를 구해 내는 프로그램을 작성하시오.
!=입력!=
첫째 줄에 N(1 ≤ N ≤ 1,000), M(1 ≤ M ≤ 1,000)이 주어진다.
다음 N개의 줄에 M개의 숫자로 맵이 주어진다.
(1, 1)과 (N, M)은 항상 0이라고 가정하자.

!=출력!=
첫째 줄에 최단 거리를 출력한다. 불가능할 때는 -1을 출력한다.
<- 예시1 ->  결과 : 15
6 4
0100
1110
1000
0000
0111
0000
<- 예시2 ->  결과 : -1
4 4
0111
1111
1111
1110
'''

from collections import deque

n, m = map(int, input().split())
arr = [list(map(int, input())) for _ in range(n)]  # 맵
visit = [[[0] * 2 for _ in range(m)] for _ in range(n)]  # 벽의 상태까지 포함된 방문 배열

# 방향 벡터
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    queue = deque()
    queue.append((0, 0, 0))  # (0,0)과 0(벽을 부순적 없음)을 큐에 넣음
    visit[0][0][0] = 1  # 시작점도 카운트
    while queue:
        x, y, status = queue.popleft()
        if x == n - 1 and y == m - 1:  # 큐에서 뽑은 좌표가 제일 끝 좌표인 경우
            return visit[x][y][status]  # 값 리턴
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:  # 인접한 값이 지도 안에 있을 경우
                if arr[nx][ny] == 1 and status == 0:  # 벽을 만났는데 벽을 부순적이 없는 경우
                    visit[nx][ny][status + 1] = visit[x][y][status] + 1  # 벽 부순 상태(1)의 값에 경로수를 추가
                    queue.append((nx, ny, status + 1))
                if arr[nx][ny] == 0 and visit[nx][ny][status] == 0:  # 벽이 없고, 방문한 적이 없는 경우
                    visit[nx][ny][status] = visit[x][y][status] + 1  # 경로 추가
                    queue.append((nx, ny, status))
    return -1  # 반복문을 통해 x,y의 좌표가 (n,m)에 도달하지 못한 경우 -1 리턴


print(bfs())
