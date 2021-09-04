'''
    1로 만들기
    정수 X가 주어졌을 때, 정수 X에 사용할 수 있는 연산은 다음과 같이 4가지입니다.
        1. X가 5로 나누어 떨어지면, 5로 나눕니다.
        2. X가 3으로 나누어 떨어지면, 3으로 나눕니다.
        3. X가 2로 나누어 떨어지면, 2로 나눕니다.
        4. X에서 1을 뺍니다.
    정수 X가 주어졌을 때, 연산 4개를 적절히 사용해서 값을 1로 만들고자 합니다. 연산을
    사용하는 횟수의 최솟값을 출력하세요. 예를 들어 정수가 26이면 다음과 같이 계산해서
    3번의 연산이 최솟값입니다.
        26 -> 25 -> 5 -> 1

    풀이 시간 20분 / 시간 제한 1초 / 메모리 제한 128MB
    입력 조건. 첫째 줄에 정수 X가 주어집니다. (1 <= X <= 30,000)
    출력 조건. 첫째 줄에 연산을 하는 횟수의 최솟값을 출력합니다.
    입력 예시 : 26
    출력 예시 : 3
'''

# 정수 x입력 받기
x = int(input())

# 값을 담을 dp 테이블 초기화
d = [0] * 30001   # d[0]은 사용 x / d[1]은 원하는 목표값.

# 다이나믹 프로그래밍 진행(바텀업 방식)
for i in range(2, x+1):
    # 1을 빼는 경우
    d[i] = d[i-1] + 1
    # 2로 나누어 떨어지는 경우
    if i % 2 == 0:
        d[i] = min(d[i], d[i//2]+1)
    if i % 3 == 0:
        d[i] = min(d[i], d[i//3]+1)
    if i % 5 == 0:
        d[i] = min(d[i], d[i//5]+1)

print(d[x])

