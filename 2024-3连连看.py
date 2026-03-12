n,m = map(int,input().split())
arr = []
for i in range(n):
      row = list(map(int,input().split()))
      arr.append(row)

pos = {}
for i in range(n):
  for j in range(m):
    val = arr[i][j]
    if val not in pos:
        pos[val] = []
    pos[val].append((i, j))

ans = 0

# 遍历每个数字的所有位置对
for val in pos:
    lst = pos[val]
    k = len(lst)
    for i in range(k):
        a, b = lst[i]
        for j in range(i + 1, k):
            c, d = lst[j]
            if abs(a - c) == abs(b - d) > 0:
                ans += 2

print(ans)