'''
    실전에서 유용한 표준 라이브러리
    itertools : 파이썬에서 반복되는 형태의 데이터를 처리하기 위한 유용한 기능을 제공
        특히 순열과 조합 라이브러리는 코딩 테스트에서 자주 사용된다.
    heapq: 힙 자료구조를 제공한다
        일반적으로 우선순위 큐 기능을 구현하기 위해 사용
    bisect: 이진 탐색(Binary search)기능을 제공한다.
    collections : 덱(deque), 카운터(Counter) 등의 유용한 자료구조를 포함한다.
    math : 필수적인 수학적 기능을 제공한다.
        팩토리얼, 제곱근, 최대공약수, 삼삭함수 관련 함수부터 파이와 같은 상수를 포함한다.
'''

# sum(), min(), max()
from itertools import permutations, combinations

result = sum([1, 2, 3, 4, 5])
print(result)

# eval() : 사람의 입장에서 사용되는 수식을 계산해 반환
result = eval("2*(2+2)")
print(result)

# sorted()
result = sorted([7, 2, 6, 9, 4])
reverse_result = sorted([7, 2, 6, 9, 4], reverse=True)
print(result)
print(reverse_result)

# sorted() with key
array = [('a', 40), ('b', 32), ('c', 23)]
print(sorted(array, key=lambda x: x[1]))

# 순열 & 조합
# from itertools import permutations
data = ['A', 'B', 'C']

result = list(permutations(data, 3))
print(result)
result = list(combinations(data, 2))
print(result)

from collections import Counter
counter = Counter(['red', 'red', 'blue', 'blue', 'red', 'black'])

print(counter['blue'])
print(counter['red'])
print(dict(counter))

import math

def lcm(a,b):
    return a * b // math.gcd(a,b)

a = 21
b = 14

print(math.gcd(21,14))
print(lcm(21,14))

