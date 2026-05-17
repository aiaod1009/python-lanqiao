n = int(input().strip())
a = [0]+list(map(int,input().split()))
s = [0]*len(a)
for i in range(1,n+1):
    s[i] = s[i-1] + a[i]

t = s[n] // 3
cnt = 0
ans = 0
if s[n] % 3 != 0:
    print(0)
else:
    for i in range(2,n):
        if s[i-1] == t:
            cnt += 1
        if s[i] == 2 * t:
            ans += cnt
    print(ans)

#只能过70%
ans = 0
for i in range(n-2):
    for j in range(i+1,n-1):
        if s[i] == s[j]-s[i] == s[n-1]-s[j]:
            ans += 1
print(ans)