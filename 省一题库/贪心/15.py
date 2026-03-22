s = input().strip()
m = max(s)
n = 0
for i in range(len(s)):
    if s[i] == m:
        n += 1
print(m*n)