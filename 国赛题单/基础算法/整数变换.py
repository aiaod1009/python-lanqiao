#只能过65%，字符串比较慢
n = int(input().strip())
ans=0
while n>0:
    s = str(n)
    x = 0
    for i in s:
        x += int(i)
    n -= x
    ans += 1
print(ans)

n = int(input().strip())
ans = 0
while n > 0:
    x = 0
    t = n
    while t > 0:
        x += t % 10
        t //= 10
    n -= x
    ans += 1
print(ans)