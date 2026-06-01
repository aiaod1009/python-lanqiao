import sys
input = lambda:sys.stdin.readline().strip()
t = int(input())
for _ in range(t):
    n,m = map(int,input().split())
    ans = 0
    # for y in range(1,m+1):
    #     for x in range(1,y):
    #         if n % x == n % y:
    #             ans = 1
    for i in range(1, m + 1):
        if (n + 1) % i != 0:
            ans = 1
            break
    print("No" if ans == 0 else "Yes")
