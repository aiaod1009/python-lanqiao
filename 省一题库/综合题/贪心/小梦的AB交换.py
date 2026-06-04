import sys
input = lambda:sys.stdin.readline().strip()
t = int(input())
for _ in range(t):
    ans = 0
    ans2 = 0
    n = int(input())
    s = input()
    s1 = 'AB'*n
    s2 = 'BA'*n
    for i in range(n*2):
        if s[i] != s1[i]:
            ans += 1
        if s[i] != s2[i]:
            ans2 += 1
    print(min(ans,ans2) // 2)