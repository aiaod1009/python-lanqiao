暴力代码
n,c = map(int,input().split())
s = list(map(int,input().split()))
ans = 0
for j in range(n):
    for i in range(n):
        if s[i] - s[j] == c:
            ans += 1
print(ans)

