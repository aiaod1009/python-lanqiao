import math,sys
input = lambda:sys.stdin.readline().strip()
k = int(input())
t = int(input())
cnt = [0] * 1000000
top,r = 1,0
while r < 1000000:
    l = r + 1
    r = l + k
    while math.gcd(l,r) != 1:
        r += 1
    cnt[l:r+1] = [top] * (r-l+1)
    top += 1
for _ in range(t):
    n = int(input())
    print(cnt[n])