# 会超时，只能部分ac
# n,m = map(int,input().split())
# arr = []
# for i in range(n):
#       row = list(map(int,input().split()))
#       arr.append(row)
#
# pos = {}
# for i in range(n):
#   for j in range(m):
#     val = arr[i][j]
#     if val not in pos:
#         pos[val] = []
#     pos[val].append((i, j))
#
# ans = 0
#
# # 遍历每个数字的所有位置对
# for val in pos:
#     lst = pos[val]
#     k = len(lst)
#     for i in range(k):
#         a, b = lst[i]
#         for j in range(i + 1, k):
#             c, d = lst[j]
#             if abs(a - c) == abs(b - d) > 0:
#                 ans += 2
#
# print(ans)


n, m = map(int, input().split())
a = [[0] * m for _ in range(n)]  # 直接开n行m列，0下标

for i in range(n):
    row = list(map(int, input().split()))
    for j in range(m):
        a[i][j] = row[j]  # 直接对应，不用j-1

ans = 0
for i in range(n):
    for j in range(m):
        for ii in range(n):
            for jj in range(m):
                # 条件完全不变，只是下标从0开始
                if a[i][j] == a[ii][jj] and abs(i - ii) == abs(j - jj) and abs(i - ii) > 0:
                    ans += 1

print(ans)