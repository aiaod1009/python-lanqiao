a = input().strip()
b = input().strip()
n = len(a)

ans = 0
lst = -1
state = -1  # 1: 仅上行, 2: 仅下行, 3: 双行贯通

for i in range(n):
    # 跳过全空白列
    if a[i] == '.' and b[i] == '.':
        continue
    # 补两个#列之间的横向空白
    if lst != -1:
        ans += i - lst - 1
    # 状态转移
    if a[i] == '#' and b[i] == '#':
        state = 3
    elif a[i] == '#' and b[i] == '.':
        if state == 2:
            ans += 1
            state = 3
        else:
            state = 1
    elif a[i] == '.' and b[i] == '#':
        if state == 1:
            ans += 1
            state = 3
        else:
            state = 2
    # 更新上一个#列
    lst = i

print(ans)