s = input().strip()
res = []
for c in s:
    if c.islower():
        res.append(chr(ord(c)-32))
    else:
        res.append(c)
print(''.join(res))

#一行流：
# print(s.upper())