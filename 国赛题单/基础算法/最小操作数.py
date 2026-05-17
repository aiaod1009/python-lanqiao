n = int(input().strip())
a = [0]+list(map(int,input().split()))+[0]
c = [0] * len(a)
for i in range(1,n+1):
    a[i] = a[i] - 1
for i in range(1,n+1):
    c[i] = a[i] - a[i-1]
ans = 0
for i in c:
    if i > 0:
        ans += i
print(ans)