s = list(input())

while True:
    n = len(s)
    new_s = []
    for i in range(n):
        if i == 0 or i == n - 1:
            new_s.append(s[i])
        else:
            left = (s[i] == s[i - 1])
            right = (s[i] == s[i + 1])
            # 只有不是边缘字符，才添加到 new_s
            if not ((left and not right) or (not left and right)):
                new_s.append(s[i])

    # 如果新字符串和旧的一样，说明稳定了
    if new_s == s:
        break
    s = new_s

print(''.join(s) if s else "EMPTY")