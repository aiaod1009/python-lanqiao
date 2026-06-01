#每人拥有的符文石数量
n=int(input())
#s表示小蓝的石头，
s=[0]+list(map(int,input().strip().split()))
t=[0]+list(map(int,input().strip().split()))
ans=0
def check(a,b):
    sa=str(a)
    sb=str(b)
    if '2' in sa and '2' in sb:
        return True
    if '4' in sa and '4' in sb:
        return True
    if '0' in sa and '0' in sb:
        return True
    return False

dp=[[1]*2 for i in range(n+1)]



for i in range(1,n+1):
    for j in range(1,i):
        if check(s[i],t[j])==True:
            dp[i][0]=max(dp[i][0],dp[j][1]+1)
            ans=max(ans,dp[i][0])
        if check(t[i],s[j])==True:
            dp[i][1]=max(dp[i][1],dp[j][0]+1)
            ans=max(ans,dp[i][1])

print(ans)