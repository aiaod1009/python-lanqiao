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