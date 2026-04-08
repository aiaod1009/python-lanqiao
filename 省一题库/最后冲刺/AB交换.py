import sys
input = lambda:sys.stdin.readline().strip()
t = int(input())
for _ in range(t):
    n, s = int(input()), input()
    a = b = 0
    for i in range(len(s)):
        # 模式1:ABABAB
        if i % 2 == 0 and s[i] != 'A': a += 1
        if i % 2 == 1 and s[i] != 'B': a += 1
        # 模式2:BABABA
        if i % 2 == 0 and s[i] != 'B': b += 1
        if i % 2 == 1 and s[i] != 'A': b += 1
    print(min(a, b) // 2)


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
