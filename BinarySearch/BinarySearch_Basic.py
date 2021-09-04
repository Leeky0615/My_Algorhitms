'''
    이진 탐색 알고리즘
        정렬되어있는 리스트에서 특정한 데이터를 빠르게 탐색할 수 있도록 하는 알고리즘
    순차 탐색
        리스트 안에 있는 특정한 데이터를 찾기 위해 앞에서부터 데이터를 하나씩 확인하는 방법
        가장 기본적인 형태의 데이터 탐색 알고리즘.
        매 단계마다 가장 작은 크기의 데이터를 찾는 과정도 이러한 순차탐색을 이용한 것이라고
        할 수 있다.
    이진 탐색
        정렬되어 있는 리스트에서 탐색 범위를 절반씩 좁혀가며 데이터를 탐색하는방법
         - 이진 탐색은 시작점, 끝점, 중간점을 이용하여 탐색 범위를 설정한다.
        로그시간의 시간 복잡도를 가질 수 있다.
    시간 복잡도
        단계마다 탐색 범위를 2로 나누는 것과 동일하므로 연산 횟수는 (log 2의 N) 에 비례한다.
'''


# 순차 탐색 소스코드 구현
def sequential_search(n, target, array):
    # 각 원소를 하나씩 확인하여
    for i in range(n):
        # 현재의 원소가 찾고자 하는 우너소와 동일한 경우
        if array[i] == target:
            # 현재의 위치 반환(인덱스는 0부터 시작)
            return i + 1


# print("생성할 원소 개수를 입력한 다음 한 칸을 띄고 찾을 문자열을 입력하세요.")
# input_data = input().split()
# 원소의 개수
# n = int(input_data[0])
n = 5
# 찾고자 하는 문자열
# target = input_data[1]
target = 'Dongbin'

# print("앞서 적은 원소 개수만큼 문자열을 입력하세요. 구분은 띄어쓰기 한 칸으로 합니다.")
# array = input().split()
array = ['Hanul', 'Jonggu', 'Dongbin', 'Taeil', 'Sangwook']
# 순차 탐색 수행 결과 출력
print(sequential_search(n, target, array))


# 이진 탐색 소스코드 구현 (반복문)
def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        # 찾은 경우 중간점 인덱스 반환
        if array[mid] == target:
            return mid
        # 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
        elif array[mid] > target:
            end = mid - 1
        # 중간점의 값보다 찾고자 하는 값이 큰 경우 오른쪽 확인
        else:
            start = mid + 1
    return None


# n(원소의 개수)과 target(찾고자 하는 값)을 입력 받기
# n, target = list(map(int, input().split()))
n = 10
target = 7
# 전체 원소 입력 받기
# array = list(map(int, input().split()))
array = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
# 이진 탐색 수행 결과 출력
result = binary_search(array, target, 0, n - 1)
if result == None:
    print("원소가 존재하지 않습니다")
else:
    print(result + 1)

'''
    파이썬 이진 탐색 라이브러리
    bisect_left(a, x) : 정렬된 순서를 유지하면서 배열 a에 x를 삽입할 가장 왼쪽 인덱스를 반환
    bisect_right(a, x) : 정렬된 순서를 유지하면서 배열 a에 x를 삽입할 가장 오른쪽 인덱스를 반환
'''

from bisect import bisect_left, bisect_right


# 값이  [left_value, reght_value]인 데이터의 개수를 반환하는 함수
def count_by_range(a, left_value, right_value):
    right_index = bisect_right(a, right_value)
    left_index = bisect_left(a, left_value)
    return right_index - left_index


# 배열 선언
a = [1, 2, 3, 3, 3, 3, 4, 4, 8, 9]

# 값이 4인 데이터 개수 출력
print("값이 4인 데이터 개수 : ",count_by_range(a, 4, 4))

# 값이 [-1,3]인 범위에 있는 데이터 개수 출력
print("값이 [-1, 3]인 범위에 있는 데이터 개수 : ", count_by_range(a, -1, 3))


'''
    파라메트릭 서치(Parametric Search)
    최적화 문제를 결정문제(예/아니오)로 바꾸어 해결하는 기법이다.
      최적화 문제 : 어떤 함수의 값을 최대한 낮추거나 높이는 문제
      이런 문제를 해결하기 어려운 경우 여러번에 결정 문제로 바꾸어 찾는다.
      ex) 특정한 조건을 만족하는 가장 알맞은 값을 빠르게 찾는 최적화 문제
          탐색 범위를 좁혀 가며 알맞은 값을 찾는다.
    일반적으로 코딩 테스트에서 파라메트릭 서치 문제는 이진 탐색을 이용하여 해결할 수 있다
'''