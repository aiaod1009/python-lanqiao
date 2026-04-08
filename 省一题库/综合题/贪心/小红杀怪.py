a,b,x,y = map(int,input().split())
ans = 10**9
for k in range(21):
    ans = min(ans, k + (max(a-k*y,0)+x-1)//x + (max(b-k*y,0)+x-1)//x)
print(ans)