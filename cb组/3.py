t = int(input().strip())
for _ in range(t):
    n, x, y = map(int, input().split())
    if x <= y:
        print(y - x + 1)
    else:
        print(0)