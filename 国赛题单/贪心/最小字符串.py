n,m = map(int,input().split())
s = input().strip()
c = input().strip()
cs = sorted(c)
i = 0
j = 0
res = []
while i < n and j < m:
    if cs[j] < s[i]:
        res.append(cs[j])
        j += 1
    else:
        res.append(s[i])
        i += 1
res.extend(s[i:])
res.extend(cs[j:])
print(''.join(res))