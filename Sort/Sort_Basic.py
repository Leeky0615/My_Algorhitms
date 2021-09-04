'''
    정렬이란 데이터를 특정한 기준에 따라 순서대로 나열하는 것을 말한다.
    일반적으로 문제 상황에 따라서 적절한 정렬 알고리즘 공식처럼 사용된다.
      데이터의 개수가 적을때, 많지만 범위가 한정되어 있을때, 이미 정렬되어 있는 경우 등에
      따라서 적절한 정렬알고리즘이 공식처럼 사용된다.

    정령을 수행하는 프로그램을 작성할 때는 정확히 어떤 방식으로 정렬을 수행할 수 있을지
    알고리즘을 코드를 이용해 정확히 표현해야한다

    1. 선택 정렬
        처리되지 않은 데이터 중에서 가장 작은 데이터를 선택해 맨 앞에 있는 데이터와
        바꾸는 것을 반복한다.
        N번 만큼 가장 작은 수를 찾아서 맨 앞으로 보내야하기 때문에
        시간 복잡도
            N + (N-1) + ... + 2 = n^2+... -> O(N^2)

    2. 삽입 정렬
        처리되지 않은 데이터를 하나씩 골라 적절한 위치에 삽입한다.
        데이터를 하나씩 확인하면서 이 데이터를 어느 위치에 넣는게 적절한 것인지
        매번 계산을 한다.
        선택 정렬에 비해 어렵지만 더 빠르게 동작한다.
        시간 복잡도는 O(N^2)이다. 하지만 현재 리스트의 데이터가 거의 정렬되어 있는
        상태라면 매우 빠르게 동작한다. 최선의 경우 O(N)의 시간 복잡도를 갖는다.

    3. 퀵 정렬
        데이터의 특성과 관련없이 표준적으로 사용할 수 있는 정렬 알고리즘이다.
        기준 데이터를 설정하고 그 기준보다 큰 데이터와 작은 데이터의 위치를 바꾸는 방법이다.
        병합 벙렬과 더불어 대부분의 프로그래밍 언어의 정렬 라이브러리의 근간이 된다.
        가장 기본적인 퀵 정렬은 첫 번째 데이터를 기준 데이터(pivot)로 설정한다.
        퀵 정렬이 빠른 이유
            데이터가 분할될 때마다 분할이 절반씩 일어난다면 전체 연산 횟수로 O(NlogN)을 기대
        하지만 최악의 경우 O(N^2)의 시간 복잡도를 갖는다.

    4. 계수 정렬
        특정한 조건이 부합할 때만 사용할 수 있지만 매우 빠르게 동작하는 정렬 알고리즘이다.
            데이터 크기 범위가 제한되어 정수 형태로 표현할 수 있을때 사용가능
        데이터의 개수가 N, 데이터 중 최댓값이 K일 때 최악의 경우에도 수행시간
        O(N+K)를 보장한다.
        공간 복잡도 또한, 가장 큰 데이터인 K를 더한만큼 O(N+K)이다.
        극단적으로 데이터가 0,999,999 2개만 있는 경우 999,999인 공간을 만들어야 하기 때문에
        비효율적이다.
        계수 정렬은 동일한 값을 가지는 데이터가 여러개 등장할 떄 효과적으로 사용할 수 있다.

'''

# 선택 정렬
print('---------- 선택 정렬 -----------')

quick_array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
for i in range(len(quick_array)):
    min_index = i  # 가장 작은 원소의 인덱스
    for j in range(i + 1, len(quick_array)):
        if quick_array[min_index] > quick_array[j]:
            min_index = j
    quick_array[i], quick_array[min_index] = quick_array[min_index], quick_array[i]
    print(quick_array)
print(quick_array)

# 삽입 정렬
print('---------- 삽입 정렬 -----------')

quick_array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
for i in range(1, len(quick_array)):
    for j in range(i, 0, -1):  # 인덱스 i부터 0까지 1씩 감소하며 반복하는 문법
        if quick_array[j] < quick_array[j - 1]:
            quick_array[j], quick_array[j - 1] = quick_array[j - 1], quick_array[j]
        else:
            break
    print(quick_array)

# 퀵 정렬
print('---------- 퀵 정렬(보통 버전) -----------')

quick_array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]


def quick_sort(array, start, end):
    if start >= end:
        return
    pivot = start
    left = start + 1
    right = end
    while left <= right:
        while left <= end and array[left] <= array[pivot]:
            left += 1
        while right > start and array[right] >= array[pivot]:
            right -= 1
        if left > right:
            array[right], array[pivot] = array[pivot], array[right]
        else:
            array[left], array[right] = array[right], array[left]
    quick_sort(array, start, right - 1)
    quick_sort(array, right + 1, end)


quick_sort(quick_array, 0, len(quick_array) - 1)
print(quick_array)

# 퀵 정렬
print('---------- 퀵 정렬(리스트 컴프리헨션 버전) -----------')

quick_array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array):
    if len(array) <= 1:
        return array
    pivot = array[0]
    tail = array[1:]

    left_side = [x for x in tail if x <= pivot]
    right_side = [x for x in tail if x > pivot]

    return quick_sort(left_side) + [pivot] + quick_sort(right_side)


print(quick_sort(quick_array))

# 계수 정렬
print('---------- 계수 정렬 -----------')

array = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]
count = [0] * (max(array) +1)

for i in range(len(array)):
    count[array[i]] += 1

for i in range(len(count)):
    for j in range(count[i]):
        print(i, end=' ') # 띄어쓰기를 구분으로 등장한 횟수만큼 인덱스 출력
print()

# 선택 정렬과 기본 정렬 라이브러리 수행 시간 비교
from random import randint
import time

# 배열에 10,000개의 정수를 삽입
array = []
for _ in range(10000):
    # 1부터 100사이의 랜덤한 정수
    array.append(randint(1, 100))

# 선택 정렬 프로그램 성능 측정
start_time = time.time()

# 선택 정렬 프로그램 소스코드
for i in range(len(array)):
    min_index = i # 가장 작은 우너소의 인덱스
    for j in range(i+1, len(array)):
        if array[min_index] > array[j]:
            min_index = j
    array[i],array[min_index] = array[min_index], array[i]

# 측정 종료
end_time = time.time()
# 수행 시간 출력
print("선택 정렬 성능 측정 : ", end_time - start_time)

# 배열을 다시 무작위 데이터로 초기화
array = []
for _ in range(10000):
    # 1부터 100사이의 랜덤한 정수
    array.append(randint(1, 100))

# 선택 정렬 프로그램 성능 측정
start_time = time.time()

# 기본 정렬 라이브러리 사용
array.sort()

# 측정 종료
end_time = time.time()
# 수행 시간 출력
print("기본 정렬 라이브러리 성능 측정 : ", end_time - start_time)