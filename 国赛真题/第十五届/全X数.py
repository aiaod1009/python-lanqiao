MOD = 998244353
n = int(input())
l,md = float('inf'),-1
cur = 0
for k in range(1,n+1):
    cur = (cur * 10 + 1)%n
    for d in range(1,10):
        if (d*cur) % n == 0:
            l,md = k,d
            break
    if md != float('inf'):
        break
if l == float('inf'):
    print(-1)
else:
    val = 0
    for _ in range(l):
        val = (val * 10 + 1) %MOD
    print((md*val) % MOD)
#暴力
n = int(input())
# 从1位、2位、3位……依次生成全相同数字的数
length = 1
while length <= 5000:  # 限制最长5000位
    # 生成当前长度下：111...1 、222...2 ... 999...9
    for d in range(1, 10):
        num = int(str(d) * length)
        if num % n == 0:
            print(num)
            exit()
    length += 1

print(-1)