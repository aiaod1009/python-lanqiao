n = int(input())
a = list(map(int,input().split()))
# l = [0] * n
# r = [0] * n
# l[0] = a[0]
# r[-1] = a[-1]
# for i in range(n):
#     l[i] = max(a[i],l[i-1]+a[i])
# for i in range(n-2,-1,-1):
#     r[i] = max(a[i],r[i]+a[i])
# ans = [l[i] + r[i] -a[i] for i in range(n)]
# print(max(ans))

#以现在这个数结尾的最大子数组和
cur = maxs = a[0]
for x in a[1:]:
    cur = max(x, cur + x)
    maxs = max(maxs, cur)
print(maxs)