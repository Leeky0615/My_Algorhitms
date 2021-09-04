from collections import deque

t = int(input())  # 테스트 케이스 개수

dx = [-1, 1, 2, 2, 1, -1, -2, -2]  # 나이트의 x좌표 이동
dy = [2, 2, 1, -1, -2, -2, -1, 1]  # 나이트의 y좌표 이동

'''
나이트의 이동 가능한 모든 경우 탐색 -> BFS 탐색
'''
def moveKnights():
    queue = deque()
    queue.append((kx, ky))  # 나이트의 좌표 넣음
    chess[kx][ky] = 1  # 나이트 좌표값 -> 1
    while queue:
        x, y = queue.popleft()  # 큐에서 원소하나를 꺼냄
        if x == mx and y == my:  # 꺼낸 좌표가 결과 좌표와 같은 경우
            return chess[x][y] - 1  # 결과값-1 리턴 :: 초기 나이트의 좌표값=1
        '''
        8방향(나이트가 이동가능한 방향)에 대해 이동한 좌표(nx,ny)가 
        체스판 안에 있고(0<= point < l)
        아직 이동한적이 없는 좌표라면(result = 0)
        '''
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < l and 0 <= ny < l and chess[nx][ny] == 0:
                queue.append((nx, ny))  # 큐에 새로운 좌표를 담음
                chess[nx][ny] = chess[x][y] + 1  # 새로운 좌표에 이동하기전 좌표값+1 넣음


for _ in range(t):
    l = int(input())  # 한 변의 길이
    (kx, ky) = map(int, input().split())  # 나이트 좌표
    (mx, my) = map(int, input().split())  # 이동하려는 좌표
    if kx == mx and ky == my:  # 나이트 좌표와 결과 좌표가 같은 경우
        print(0)  # 0 출력
    else:
        chess = [[0] * l for _ in range(l)]  # 체스판 모든 칸 -> 0
        print(moveKnights())
