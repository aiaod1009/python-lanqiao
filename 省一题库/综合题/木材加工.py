import sys
input = lambda :sys.stdin.readline().strip()
n,k = map(int,input().split())
a = [int(input()) for _ in range(n)]
l = 0
r = max(a)
ans = 0
while l <= r:
    mid = (l + r) // 2
    if mid == 0:
        l = mid + 1
        continue
    cnt = sum(x // mid for x in a)
    if cnt >= k:
        ans = mid
        l = mid + 1
    else:
        r = mid - 1
print(ans)

