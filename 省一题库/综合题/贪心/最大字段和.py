n = int(input())
a = list(map(int,input().split()))
# l = [0] * n
# l[0] = a[0]
# for i in range(1,n):
#     l[i] = max(a[i],l[i-1]+a[i])
# print(max(l))

#以现在这个数结尾的最大子数组和
cur = maxs = a[0]
for x in a[1:]:
    cur = max(x, cur + x)
    maxs = max(maxs, cur)
print(maxs)