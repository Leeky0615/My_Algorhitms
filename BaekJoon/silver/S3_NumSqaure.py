n, m = map(int, input().split())
arr = [list(map(int, input())) for _ in range(n)]
size = 0;
for i in range(n):
    for j in range(m):
        for k in range(min(n, m)):
            if i + k < n and j + k < m:
                if arr[i][j] == arr[i + k][j] == arr[i][j + k] == arr[i + k][j + k]:
                    size = max(size, (k + 1) ** 2)

print(size)
