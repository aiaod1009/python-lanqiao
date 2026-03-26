import sys
input = lambda:sys.stdin.readline()
n = int(input())
a = list(map(int,input().split()))
q = int(input())
# for i in range(q):
#     m = int(input().strip())
#     ans = 0
#     for j in range(n):
#         if m == a[j]:
#             ans = j+1
#             break
#     print(ans)


# 哈希法
# pos = {value: index+1 for index, value in enumerate(a)}
pos = {}
for i in range(n):
    pos[a[i]] = i + 1
for i in range(q):
    m = int(input().strip())
    print(pos.get(m, 0))  # 找到返回位置，找不到返回0


# 二分法
import bisect
arr = []
for i in range(n):
    arr.append((a[i], i+1))
arr.sort()
values = [x[0] for x in arr]
for _ in range(n):
    m = int(input().strip())
    idx = bisect.bisect_left(values,m)
    if idx < n and values[idx] == m:
        print(arr[idx][1])
    else:
        print(0)