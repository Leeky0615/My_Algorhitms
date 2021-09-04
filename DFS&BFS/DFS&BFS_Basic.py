'''
    DFS & BFS
        대표적인 그래프 탐색 알고리즘으로 탐색이란 많은 양의 데이터 중에서 원하는
        데이터를 찾는 과정을 말한다.
        특정 조건에 맞는 데이터가 존재하는지, 존재한다면 어느 위치에 있는지 탐색
        대표적인 탐색 알고리즘으로 DFS, BFS가 있다.
        코딩테스트에서 매우 자주 등장하는 유형이다.

    스택 자료구조
        먼저 들어온 데이터가 나중에 나가는 형식의 자료구조이다.
        입구와 출구가 동일한 형태로 스택을 시각화할 수 있다.
'''

# 스택 구현 예제
stack = []

stack.append(5)
stack.append(2)
stack.append(3)
stack.append(7)
stack.pop()
stack.append(1)
stack.append(4)
stack.pop()

print(stack[::-1])  # 최상단 원소부터 출력
print(stack)  # 최하단 원소부터 출력

'''
    큐 자료구조 
        먼저 들어온 데이터가 먼저 나가는 형식의 자료구조이다.
        큐는 입구와 출구가 모두 뚫려 있는 터널과 같은 형태로 시각화할 수 있다.
'''

from collections import deque

# 큐 구현을 위해 deque 라이브러리 사용
queue = deque()

queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft()
queue.append(1)
queue.append(4)
queue.popleft()

print(queue)  # 먼저 들어운 순서대로 출력
queue.reverse()  # 역순으로 바꾸기
print(queue)  # 나중에 들어온 원소부터 출력

'''
    재귀 함수
        자기 자신을 다시 호출하는 함수
        DFS를 실질적으로 구현하고자 할 때 자주 사용되는 방법중 하나이다.
        파이썬에서는 재귀함수 호출 개수의 제한이 있기 때문에 제한을 두어야 한다.
        재귀 함수를 문제 풀이에서 사용할 때에는 재귀함수의 종료 조건을 반드시
        명시해야한다.
'''


# 재귀 함수 예시
# def recursive_function():
#     print('재귀 함수를 호출합니다.')
#     recursive_function()
#
# recursive_function()

# 종료 조건을 포함한 재귀 함수 예제
def recursive_func(i):
    if i == 5: return
    print(i, '번째 재귀함수에서', i + 1, '번째 재귀함수를 호출합니다.')
    recursive_func(i + 1)
    print(i, '번째 재귀함수를 종료합니다.')


recursive_func(1)


# 팩토리얼 구현 예제

# 반복적으로 구현한 n!
def factorial_iterative(n):
    result = 1
    # 1 부터 n가지의 수를 차례대로 곱하기
    for i in range(1, n + 1):
        result *= i
    return result


# 재귀적으로 구현한 n!
def factorial_recursive(n):
    if n <= 1:  # n이 1 이하인 경우 1을 반환
        return 1
    # n! = n * (n-1)!를 그대로 코드로 작성하기
    return n * factorial_recursive(n - 1)


# 각각의 방식으로 구현한 n! 출력(n=5)
print('반복적으로 구현:', factorial_iterative(5))
print('재귀적으로 구현:', factorial_recursive(5))

'''
    최대공약수 계산(유클리드 호제법) 예제
    유클리드 호제법
        두 자연수에 대하여 A를 B를 나눈 나머지를 R이라고 한다
        이때 A와 B의 최대공약수는 B와 R의 최대공약수와 같다.
'''

def gcd(a, b):
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)

print(gcd(192, 162))

'''
    재귀 함수 사용의 유의사항
      재귀 함수를 잘 활용하면 복잡한 알고리즘을 간결하게 작성할 수 있다.
        단 오히려 다른 사람이 이해하기 어려운 형태의 코드가 될 수 있다
      모든 재귀 함수는 반복문을 이용하여 동일한 기능을 구현할 수 있다.
      재귀 함수가 반복문보다 유리한 경우도 있고 불리한 경우도 있다.
      컴퓨터가 함수를 연속적으로 호출하면 컴퓨터 메모리 내부의 스택 프레임에 쌓인다.
        그래서 스택을 사용해야할 때 구현상 스택 라이브러리 대신에 재귀 함수를 이용하는
        경우가 많다
'''