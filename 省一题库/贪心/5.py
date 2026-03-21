n = int(input().strip())
a = list(map(int,input().split()))
l = n // 2
c = [a[i] - a[n-1-i] for i in range(l)]

tmp = 0
for i in range(l):
    tmp += abs(c[i]) #先假设单独处理当前 c[i],需要 abs(c[i])次操作
    if c[i] > 0 and c[i+1] > 0:
        c[i + 1] -= min(c[i], c[i + 1])
    if c[i] < 0 and c[i+1] < 0:
        c[i + 1] -= max(c[i], c[i + 1])
print(tmp)

# 📌 用样例走一遍完整流程
# 样例：c[1] = -3, c[2] = -1
# i=1：
# tmp += abs(-3) → tmp = 3
# c[1] < 0 且 c[2] < 0 → 同负
# max(-3, -1) = -1
# c[2] = -1 - (-1) = 0
# i=2：
# tmp += abs(0) → tmp 保持 3
# 无同号处理
# 输出 3 ✅ 和样例完全一致
