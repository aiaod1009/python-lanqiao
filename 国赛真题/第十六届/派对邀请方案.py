mod = 10**9+7
n = 2025
cnt = {}
for i in range(1,n+1,2):
    l = 0  # 用来记录这队一共有多少人。
    curr = i # 让当前这个人站在排头。
    while curr <= n:
        l += 1
        curr *= 2
    cnt[l] = cnt.get(l,0) + 1
ans = 1
for l,c in cnt.items():
    a,b = 1,1
    for _ in range(l):
        a,b = (a+b)%mod,a  #滚动变量
    ans = (ans*pow(a,c,mod)) % mod
print(ans)