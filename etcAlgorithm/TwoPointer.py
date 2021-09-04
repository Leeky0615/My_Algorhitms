'''
    투 포인터
    투 포인터 알고리즘은 리스트에 순차적으로 접근해야 할 때 두개의 점의 위치를 기록하면서
    처리하는 알고리즘을 의미한다.
    흔히 2,3,4,5,6,7번 학생을 지목해야 할 때 간단히 '2번부터 7번까지의 학생'이라고 부른다
    리스트에 담긴 데이터에 순차적으로 접근해야할 때는 시작점과 끝점 2개의 점으로 접근할
    데이터의 범위를 표현할 수 있다.

    특정한 합을 가지는 부분 연속 수열 찾기
     - N개의 자연수로 구성된 수열이 있습니다.
     - 합이 M인 부분 연속 수열의 개수를 구해보세여
     - 수행 시간 제한은 O(N)입니다.
    투포인터를 활용하여 다음과 같은 알고리즘으로 문제를 해결할 수 있다.
     1. 시작점과 끝점이 첫 번째 원소의 인덱스(0)를 가리키도록 한다.
     2. 현재 부분 합이 M과 같다면, 카운트 한다.
     3. 현재 부분 합이 M보다 작다면, end를 1증가시킨다.
     4. 현재 부분 합이 M보다 크거나 같다면, start를 1증가시킨다.
     5. 모든 경우를 확인할 떄까지 2번부터 4번까지의 과정을 반복한다.
'''
data = [1, 2, 3, 2, 5, 6, 4, 7, 2, 5, 3]
n = 11  # 데이터의 개수 n
m = 10  # 찾고자 하는 부분합 m
print('-----------------동빈나 ver.-----------------')

count = 0
interval_sum = 0
end = 0

# start를 차례대로 증가시키며 반복
for start in range(n):
    # end를 가능한 만큼 이동시키기
    while interval_sum < m and end < n:
        interval_sum += data[end]
        end += 1
    # 부분합이 m일때 카운트 증가
    if interval_sum == m:
        count += 1
    interval_sum -= data[start]

print('결과 : ',count)


print('------------------ 내 ver.------------------')
start = 0
end = 0
count = 0
while start < n and end < n:
    interval_sum = sum(data[start:end+1])
    if interval_sum >= m:
        start += 1
        if interval_sum == m:
            count += 1
    else:
        end += 1

print('결과 : ',count)
