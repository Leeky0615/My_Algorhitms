n, a, b = map(int, input().split())
result = 0
while a != b:
    a = (a + 1) // 2
    b = (b + 1) // 2
    result += 1

print(result)
