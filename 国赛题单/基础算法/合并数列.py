n, m = map(int, input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
i = j = s1 = s2 = k = 0
# s1：数组 a 的当前前缀和
# s2：数组 b 的当前前缀和
# k：公共前缀和节点的数量
while i < n and j < m:
    if s1 == s2:
        if s1 != 0: #避免算初始的0
            k += 1
        s1 += a[i]
        s2 += b[j]
        i += 1
        j += 1
    elif s1 < s2:
        s1 += a[i]
        i += 1
    else:
        s2 += b[j]
        j += 1
# 数组 a 需要合并的次数：n - (k+1)
# 数组 b 需要合并的次数：m - (k+1)
# 总次数：(n - (k+1)) + (m - (k+1)) = n + m - 2*(k+1)
print(n + m - 2 * (k + 1))