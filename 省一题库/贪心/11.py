n,m = map(int,input().split())
p = list(map(int,input().split()))
L = min(p)
R = max(p)
res = []
for i in range(1,n+1):
    res.append(str(max(i-L,R-i)))
print(' '.join(res))


#暴力枚举方法
# 你的原始思路（枚举所有队长，算每个位置的最大距离）
n, m = map(int, input().split())
cap = list(map(int, input().split()))

# 初始化每个位置的最大距离为0
max_dist = [0] * (n + 1)  # 1-based

# 枚举每个队长
for p in cap:
    # 枚举每个位置，更新最大距离
    for i in range(1, n+1):
        dist = abs(i - p)
        if dist > max_dist[i]:
            max_dist[i] = dist

# 输出结果
print(' '.join(map(str, max_dist[1:])))