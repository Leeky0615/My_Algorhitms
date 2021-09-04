'''
    효율적인 화폐 구성
    N가지 종류의 화폐가 있습니다. 이 화폐들의 개수를 최소한으로 이용하여 그 가치의 합이
    M원이 되도록 하려고 합니다. 이때 각 종류의 화폐는 몇 개라도 사용할 수 있습니다.
    예를 들어 2원, 3원 단위의 화폐가 있을 때는 15원을 만들기 위해 3원을 5개 사용하는 것이
    가장 최소한의 화폐 개수입니다.
    M원을 만들기 위한 최소한의 화폐 개수를 출력하는 프로그램을 작성하세요.

    풀이시간 30분 / 시간 제한 1초 / 메모리 제한 128MB
    입력 조건. 첫째 줄에 N,M이 주어진다. (1 <= N <= 100, 1 <= M <= 10,000)
              이후의 N개의 줄에는 각 화폐의 가치가 주어진다. 화폐의 가치는
              10,000보다 작거나 같은 자연수이다.
    출력 조건. 첫째 줄에 최소 화폐 개수를 출력한다.
              불가능할 때는 -1를 출력한다.
    입력 예시
    2 15            3 4
    2               3
    3               5
                    7
    출력 예시
    5               -1
'''

n, m = list(map(int, input().split()))
d = [0] * 10001
array = [0] * n

for i in range(n):
    array[i] = int(input())

print(array)

for i in range(2, m + 1):
    print('------------',i,'----------------')
    temp = [0] * n
    for j in range(n):
        if i % array[j] == 0:
            temp[j] = d[i - array[j]] + 1
        else:
            temp[j] = float('inf')
    print(temp,' / 최소값 : ',min(temp))
    d[i] = min(temp)

if d[m] == float('inf'):
    print(-1)
else:
    print(d[m])


# 풀이
# 정수 N, M을 입력 받기
n,m = map(int, input().split())
# N개의 화폐 단위 정보를 입력받기
array = []
for i in range(n):
    array.append(int(input()))

# 한 번 계산된 결과를 저장하기 위한 DP 테이블 초기와
d = [10001] * (m+1)

# 다이나믹 프로그래밍 진행(바텀업)
d[0] = 0
for i in range(n):
    for j in range(array[i], m+1):
        if d[j - array[i]] != 10001: # (i-k)원을 만드는 방법이 존재하는 경우
            d[j] = min(d[j], d[j - array[i]] +1)

# 계산된 결과 출력
if d[m] == 10001:
    print(-1)
else:
    print(d[m])