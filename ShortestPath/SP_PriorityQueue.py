'''
    우선순위 큐(Priority Queue)
    우선순위가 가장 높은 데이터를 가장 먼저 삭제하는 자료구조이다.
    예를 들어, 여러개의 물건 데이터를 자료구조에 넣었다가 가치가 높은 물건 데이터부터
    꺼내서 확인해야 하는 경우에 우선순위 큐를 이용할 수 있다.
    대부분의 언어에서 표준 라이브러리 형태로 지원한다.

    힙(Heap)
    우선순위 큐를 구현하기 위해 사용하는 자료 구조중 하나이다.
    최소 힙과 최대 힙이 있다.
    삽입 하거나 삭제하는 과정에서 logN만큼의 시간복잡도가 걸린다.

    개선된 구현방법
    - 단계마다 방문하지 않은 노드 중에서 최단 거리가 가장 짧은 노드를 선택하기 위해
      힙 자료구조를 이용한다.
    - 다익스트라 알고리즘이 동작하는 기본 원리는 동일합니다.
      현재 가장 가까운 노드를 저장해 놓기 위해서 힙 자료구조를 추가적으로 이용한다는
      점이 다르다
      현재의 최단 거리가 가장 짧은 노드를 선택해야 하므로 최소 힙을 사용한다.
'''
# 최소힙
import heapq

# 오름차순 힙 정렬(Heap Sort)
def heapsort(iterable):
    h = []
    result = []
    # 모든 원소를 차례대로 힙에 삽입
    for value in iterable:
        heapq.heappush(h, value)
    # 힙에 삽입된 모든 원소를 차례대로 꺼내어 담기
    for i in range(len(h)):
        result.append(heapq.heappop(h))
    return result


result = heapsort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])
print(result)

# 최대힙 (파이썬에서 별도로 제공하지는 않음)
def heapsort2(iterable):
    h = []
    result = []
    # 모든 원소를 차례대로 힙에 삽입
    for value in iterable:
        heapq.heappush(h, -value)
    # 힙에 삽입된 모든 원소를 차례대로 꺼내어 담기
    for i in range(len(h)):
        result.append(-heapq.heappop(h))
    return result


result = heapsort2([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])
print(result)
