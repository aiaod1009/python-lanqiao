s = input().strip()
n = len(s)
i,j =0, n - 1
cnt = 0
while i < j:
    while i < j and s[i] != 'A':
        i += 1
    while i < j and s[j] != 'B':
        j -= 1
    if i < j and s[i] == 'A' and s[j] == 'B':
        cnt += 1
        i += 1
        j -= 1
print(n-2*cnt)
