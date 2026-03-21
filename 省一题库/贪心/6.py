n,m = map(int,input().split())
s = input().strip()
c = sorted(input().strip())
i = 0
j = 0
res = []
while i < n and j < m:
    if c[j] < s[i]:
        res.append(c[j])
        j += 1
    else:
        res.append(s[i])
        i += 1

