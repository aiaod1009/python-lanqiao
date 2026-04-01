a = input().strip()
b = input().strip()
n = len(a)
ans = 0
lst = -1  #上一次出现 # 的列在哪里
s = -1  # 1: 仅上行, 2: 仅下行, 3: 双行贯通

for i in range(n):
    # 跳过全空白列
    if a[i] == '.' and b[i] == '.':
        continue
    # 补两个#列之间的横向空白
    if lst != -1:
        ans += i - lst - 1
    # 状态转移
    if a[i] == '#' and b[i] == '#':
        s = 3
    elif a[i] == '#' and b[i] == '.':
        if s == 2:
            ans += 1
            s = 3
        else:
            s = 1
    elif a[i] == '.' and b[i] == '#':
        if s == 1:
            ans += 1
            s = 3
        else:
            s = 2
    lst = i

print(ans)

