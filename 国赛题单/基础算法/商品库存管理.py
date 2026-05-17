import sys
input = lambda:sys.stdin.readline().strip()
n,m=map(int,input().split())
diff =  [0]*(n+2)
l,r = [],[]
for _ in range(m):
    L,R = map(int,input().split())
    l.append(L)
    r.append(R)
    diff[L] += 1
    diff[R+1] -= 1
pre = [0]*(n+1)
sum0 = 0
cur = 0
for i in range(1,n+1):
    cur += diff[i]
    if cur == 0:
        sum0 += 1
    pre[i] = pre[i-1] + (1 if cur == 1 else 0)
for i in range(m):
    ans = pre[r[i]] - pre[l[i]-1] + sum0
    print(ans)