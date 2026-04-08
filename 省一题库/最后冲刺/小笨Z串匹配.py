import sys
input = lambda:sys.stdin.readline().strip()
t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    z = input()
    ans = 0
    for i in range(n):
        if z[i] == '>' and a[i] <= 0:
            a[i] = 1
            ans += 1
        elif z[i] == '<' and a[i] >= 0:
            a[i] = -1
            ans += 1
        elif z[i] == 'Z' and a[i-1]*a[i] <= 0:
            ans += 1
    print(ans)