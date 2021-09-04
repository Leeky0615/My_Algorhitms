from collections import deque  # deque 임포트

m, n, h = map(int, input().split())  # 가로, 세로, 높이 입력받기

# 박스(3차원 배열)에 토마토의 정보를 입력받음
box = []
for _ in range(h):
    box.append([list(map(int, input().split())) for _ in range(n)])  # 하나의 층에 있는 토마토 정보

#  방향 벡터(x,y,z 축)
dx = [0, 1, 0, -1, 0, 0]
dy = [1, 0, -1, 0, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

'''
익은 토마토(1)를 찾아 queue에 담아 리턴하는 함수
익은 토마토가 하나도 없다면 -1 리턴
'''
def findRipenTomato(arr):
    temp = deque()
    for i in range(h):  # 높이 h
        for j in range(n):  # 세로 n
            for k in range(m):  # 가로 m
                if arr[i][j][k] == 1:
                    temp.append((k, j, i))
    return temp


'''
BFS를 사용해 익은 토마토를 기준으로 
박스에 있는 토마토의 상태를 변경 -> 진행되는 일수 입력
'''
def changeTomato(arr, queue):
    while queue:
        x, y, z = queue.popleft()
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]
            if 0 <= nx < m and 0 <= ny < n and 0 <= nz < h and arr[nz][ny][nx] == 0:
                arr[nz][ny][nx] = arr[z][y][x] + 1
                queue.append((nx, ny, nz))


'''
박스에 보통 토마토가 있는지 확인하는 함수
보통 토마토(0)의 개수가 0이면 False 리턴
'''
def isTomato(arr):
    status = False
    for i in arr:
        for j in i:
            if j.count(0) != 0:
                status = True
    return status


if isTomato(box):  # 보통 토마토(0)가 존재
    queue = findRipenTomato(box)  # 익은 토마토(1)의 좌표를 큐에 넣음
    if queue:  # 익은 토마토(1)가 있는 경우
        changeTomato(box, queue)  # 토마토를 모두 익은 상태로 변경 -> BFS탐색
        if not isTomato(box):  # 보통 토마토(0) 존재 하지 않음
            result = 0
            for i in box:
                for j in i:
                    result = max(result, max(j))  # result = 박스의 모든 원소중 가장 큰 값
            print(result - 1)  # 결과값-1 출력 :: 초기 시작값을 1로 시작했기 떄문
        else:  # 보통 토마토(0)가 존재
            print(-1)  # 계속 보관 해도 모든 토마토가 익을 수 없으므로 -1 출력
    else:  # 익은 토마토(1)가 없는 경우
        print(-1)  # 익은 토마토가 없으므로 보통 토마토가 익을 수 없으므로 -1 출력
else:  # 보통 토마토(0) : 0개 -> 이미 모두 익어 있거나 상자가 모두 비어있음
    print(0)
