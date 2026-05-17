import sys
input = lambda:sys.stdin.readline().strip()
n,m,c = map(int,input().split())
a = [[0]*(m+1)]
for _ in range(n):
    i = [0]+list(map(int,input().split()))
    a.append(i)

pre = [[0]*(m+1) for _ in range(n+1)]
for i in range(1,n+1):
    for j in range(1,m+1):
        pre[i][j] = a[i][j]+pre[i-1][j]+pre[i][j-1]-pre[i-1][j-1]
t = int(input())
cycle = c+1
for _ in range(t):
    x1,y1,x2,y2,k = map(int,input().split())
    d = k % cycle
    cnt = (x2-x1+1)*(y2-y1+1)
    suma = pre[x2][y2] - pre[x1-1][y2] - pre[x2][y1-1] + pre[x1-1][y1-1]
    print(suma - d*cnt)