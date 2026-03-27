import sys
input = lambda:sys.stdin.readline().strip()
n = int(input())
s = 0
l = [0] + [-1]*6  # s[0] = 0 是前缀和的起点
r = [-1]*7
for i in range(1,n+1):
    a = int(input())
    s = (s+a) % 7
    if l[s] == -1:
        l[s] = i   # 这个余数第一次出现，记录最早位置
    r[s] = i     # 每次都更新为最后出现的位置
ans = 0
for i in range(7):
    if l[i] != -1:
        ans = max(ans,r[i] - l[i])
print(ans)

# 思路:前缀和加同余定理
#「和为 7 的倍数」转化为「两个前缀和余数相同」
# 然后对每个余数，找到它最早和最晚出现的位置
# 两者相减就是这个余数能提供的最长合法区间，所有余数的最大值就是答案。




#暴力法
n = int(input())
a = [0] * (n + 1)
for i in range(1, n+1):
    a[i] = int(input())

# 前缀和
b = [0] * (n + 1)
for i in range(1, n+1):
    b[i] = b[i-1] + a[i]

ans = 0
# 暴力枚举所有区间 [i, j]
for i in range(1, n+1):
    # 小优化：j 从 i+ans 开始，只找更长的
    for j in range(i + ans, n+1):
        if (b[j] - b[i-1]) % 7 == 0:
            ans = j - i + 1  # 更新最长长度

print(ans)