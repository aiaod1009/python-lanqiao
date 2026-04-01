# 上一题：直接求数组的最大连续和
# 这一题：求收益数组的最大连续和，再加回原价
n,x = map(int,input().split())
a = list(map(int,input().split()))
# 计算原数组总和（不操作时的基础和）
tot = sum(a)
cur = m = x - a[0] # 先把第一个数当成 “一开始选的那段区间”
for n in a[1:]:
    g = x - n  # 当前元素的替换收益（可正可负）
    cur = max(g,cur+g)
    m = max(m,cur)
print(tot+max(m,0))