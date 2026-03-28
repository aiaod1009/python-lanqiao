n = int(input().strip())
c = list(map(int,input().split()))
c.sort(reverse=True)
ans = 0
if n % 3 == 0:
    for i in range(0,n,3):
        ans +=  sum(c[i:i+3]) - min(c[i:i+3])
elif n % 3 == 1:
    for i in range(0,n-1,3):
        ans +=  sum(c[i:i+3]) - min(c[i:i+3])
    ans+=c[-1]
elif n % 3 == 2:
    for i in range(0, n - 2, 3):
        ans +=  sum(c[i:i+3]) - min(c[i:i+3])
    ans += sum(c[-2:])

print(ans)


# 简单法（都是纯贪心）
n = int(input().strip())
c = list(map(int, input().split()))
c.sort(reverse=True)  # 从大到小排

ans = 0
for i in range(n):
    if (i + 1) % 3 != 0:  # 第 3、6、9… 个免费
        ans += c[i]

print(ans)