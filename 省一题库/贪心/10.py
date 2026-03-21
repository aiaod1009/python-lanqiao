n = 2*int(input().strip())
w = sorted([0] + list(map(int,input().split())))
ans = 0
for i in range(1,n//2+1):
    ans += w[i]*w[n-i+1]
print(ans)