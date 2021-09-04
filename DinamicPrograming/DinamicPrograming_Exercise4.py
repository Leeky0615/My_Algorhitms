'''
    금광 문제
    n x m 크기의 금광이 있습니다. 금광은 1x1 크기의 칸으로 나누어져 있으며, 각 칸은
    특정한 크기의 금이 들어 있습니다.
    채굴자는 첫 번째 열부터 출발하여 금을 캐기 시작합니다. 맨 처음에는 첫 번째 열의
    어느 행에서든 출발할 수 있습니다. 이후에 m-1번에 걸쳐서 매번 오른쪽 위, 오른쪽,
    오른쪽 아래 3가지 중 하나의 위치로 이동해야 합니다. 결과적으로 채굴자가 얻을 수
    있는 금의 최대 크기를 출력하는 프로그램을 작성하세요.

    풀이 시간 30분 / 제한 시간 1초 / 메모리 제한 128MB / 기출 Filpkart 인터뷰
    입력 조건. 첫째 줄에 테스트 케이스 T가 입력됩니다. (1<=T<=1000)
              매 테스트 케이스 첫째 줄에 n과 m이 공백으로 구분되어 입력됩니다.
              (1 <= n,m <= 20) 둘째 줄에 n x m 개의 위치에 매장된 금의 개수가
              공백으로 구분되어 입력됩니다.(1<= 각 위치에 매장된 금의 개수 <= 100)
    출력 조건. 테스트 케이스마다 채굴자가 얻을 수 있는 금의 최대 크기를 출력합니다.
              각 테스트 케이스는 줄 바꿈을 이용해 구분합니다.
    입력 예시
2
3 4
1 3 3 2 2 1 4 1 0 6 4 7
4 4
1 3 1 5 2 2 4 1 5 0 2 3 0 6 1 2
    출력 예시
    19
    16
'''

# case = int(input())
# case_array = [0]*case
# for x in range(case):
#     n , m = map(int, input().split())
#     array = [[0] * m for _ in range(n)]
#     golds = list(map(int, input().split()))
#     for i in range(n):
#         for j in range(m):
#             array[i][j] = golds[(i*n)+j]
#     case_array[x] = array

for z in range(int(input())):
    n , m = map(int, input().split())
    array = list(map(int, input().split()))
    # dp 테이블 초기화
    dp = []
    index = 0
    for i in range(n):
        dp.append(array[index:index+m])
        index += m

    for j in range(1, m):
        for i in range(n):
            if i == 0:
                left_up = 0
            else:
                left_up = dp[i-1][j-1]
            if i == n-1:
                left_down == 0
            else:
                left_down = dp[i+1][j-1]
            left = dp[i-1][j]
        dp[i][j] = dp[i][j] + max(left_down, left, left_up)

    result = 0
    for i in range(n):
        result = max(result, dp[i][m-1])
    print(result)