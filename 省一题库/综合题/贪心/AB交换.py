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