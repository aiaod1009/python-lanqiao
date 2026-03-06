import os
import sys

# 请在此输入您的代码

n, length = map(int, sys.stdin.readline().split())
valves = []
for i in range(n):
    L, S = map(int, sys.stdin.readline().split())
    valves.append((L, S))

left = 0
right = 2 * 10 ** 9
ans = right

while left <= right:
    mid = (left + right) // 2
    intervals = []

    for L, S in valves:
        if mid < S:
            continue
        d = mid - S
        intervals.append((L - d, L + d))

    intervals.sort()
    current_end = 0
    for a, b in intervals:
        if a > current_end + 1:
            break
        current_end = max(current_end, b)
        if current_end >= length:
            break

    if current_end >= length:
        ans = mid
        right = mid - 1
    else:
        left = mid + 1
print(ans)