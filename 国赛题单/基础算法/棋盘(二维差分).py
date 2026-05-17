import sys
input = lambda:sys.stdin.readline().strip()
n, m = map(int, input().split())
# 差分数组多开2位，防止越界
diff = [[0] * (n + 2) for _ in range(n + 2)]
# 1. 打差分标记（O(m)）
for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    diff[x1][y1] += 1
    diff[x1][y2 + 1] -= 1
    diff[x2 + 1][y1] -= 1
    diff[x2 + 1][y2 + 1] += 1

# 2. 二维前缀和还原（O(n²)）
# 先对每行做前缀和
for i in range(1, n + 1):
    row_sum = 0
    for j in range(1, n + 1):
        row_sum += diff[i][j]
        diff[i][j] = row_sum

# 再对每列做前缀和
for j in range(1, n + 1):
    col_sum = 0
    for i in range(1, n + 1):
        col_sum += diff[i][j]
        diff[i][j] = col_sum

# 3. 输出结果：次数为奇则为1，偶则为0
for i in range(1, n + 1):
    line = ''.join(str(diff[i][j] % 2) for j in range(1, n + 1))
    print(line)



#暴力
n, m = map(int, input().split())
a = [[0] * (n + 2) for _ in range(n + 2)]
for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(x1, x2 + 1):
        for j in range(y1, y2 + 1):
            a[i][j] = 1 - a[i][j]
for i in range(1, n + 1):
    line = ''.join(str(a[i][j]) for j in range(1, n + 1))
    print(line)