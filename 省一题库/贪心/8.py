s = input().strip()
i = 0
cnt = 0
while i < len(s)-2:
    sub = s[i:i+3]
    if set(sub) == {'l','q','b'}:
        cnt += 1
        i += 3
    else:
        i += 1
print(cnt)