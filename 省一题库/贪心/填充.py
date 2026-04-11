s = input().strip()
n = len(s)
i = 0
res = 0
while i < n-1:
    if s[i] == s[i+1] or (s[i]=='?' or s[i+1]=='?'):
        res += 1
        i += 2
    else:
        i += 1
print(res)