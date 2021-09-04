'''
문제
수빈이는 동생과 숨바꼭질을 하고 있다. 수빈이는 현재 점 N(0 ≤ N ≤ 100,000)에 있고,
동생은 점 K(0 ≤ K ≤ 100,000)에 있다. 수빈이는 걷거나 순간이동을 할 수 있다. 만약,
수빈이의 위치가 X일 때 걷는다면 1초 후에 X-1 또는 X+1로 이동하게 된다. 순간이동을
하는 경우에는 1초 후에 2*X의 위치로 이동하게 된다.
수빈이와 동생의 위치가 주어졌을 때, 수빈이가 동생을 찾을 수 있는 가장 빠른 시간이 몇
초 후인지 구하는 프로그램을 작성하시오.

입력
첫 번째 줄에 수빈이가 있는 위치 N과 동생이 있는 위치 K가 주어진다. N과 K는 정수이다.

출력
수빈이가 동생을 찾는 가장 빠른 시간을 출력한다.

예제 입력 1
5 17
예제 출력 1
4

'''
# queue를 사용하기 위해 collection.deque 라이브러리 추가
from collections import deque

# 수빈, 동생위치 입력받기
n, k = map(int, input().split())
# 노드의 깊이를 담은 배열, 점의 최대 위치가 100,000이므로 크기를 100,001로 설정
arr = [0] * 100001

# bfs에 사용될 queue 생성
queue = deque()
# queue에 수빈의 위치를 넣음
queue.append(n)

# queue가 빌 때까지 반복
while queue:
    # queue에서 원소 하나를 꺼냄
    node = queue.popleft()

    # 만약 node(위치)가 k(동생위치)라면
    if node == k:
        # 해당 노드의 깊이를 출력하고 반복문 종료
        print(arr[node])
        break

    # 다음 노드 :: -1, +1, *2를 수행한 위치에 대해 노드확인
    for next_node in (node - 1, node + 1, node * 2):
        # 다음 노드의 위치가 0이상 100,001보다 작고
        # 깊이의 값이 0이라면(초기에 모든 값을 0으로 초기화, not 0 = not False = True)
        if 0 <= next_node < 100001 and not arr[next_node]:
            # 다음 노드의 위치에 현재 노드의 깊이 + 1 넣기.
            arr[next_node] = arr[node] + 1
            # queue에 다음 노드 추가.
            queue.append(next_node)
