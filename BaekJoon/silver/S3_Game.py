x, y = map(int, input().split())
count = 0
z = (y * 100) // x
nz = z

if x <= y:
    print(-1)
else:
    while z == nz:
        count += 1
        nz = ((y + count) * 100) // (x + count)

    print(count)

