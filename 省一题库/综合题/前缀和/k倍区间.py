import sys
input = lambda:sys.stdin.readline().strip()
n,k = map(int,input().split())
cnt = [0] *k
cnt[0] = 1
s = 0
ans = 0
for _ in range(n):
    a = int(input())
    s = (s+a) % k
    ans += cnt[s]
    cnt[s] += 1
print(ans)


# 思路：前缀和+同余定理



#暴力
n, k = map(int, input().split())
a = [int(input()) for _ in range(n)]

ans = 0
# 枚举所有区间 [i, j]
for i in range(n):
    current_sum = 0
    for j in range(i, n):
        current_sum += a[j]       # 累加区间和
        if current_sum % k == 0:  # 判断是否是 K 的倍数
            ans += 1

print(ans)