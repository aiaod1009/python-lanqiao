S = input().strip()
n = len(S)
Q = int(input())
# 1. 预处理所有匹配的括号对，用栈实现
stack = []
pairs = []  # 存所有 (L, R) 括号对
for i, ch in enumerate(S):
    if ch == '(':
        stack.append(i)
    elif ch == ')':
        L = stack.pop()
        pairs.append((L, i))
# 2. 处理每个查询
for _ in range(Q):
    c, x = input().split()
    x = int(x)
    ans = 0
    # 遍历每一对括号
    for L, R in pairs:
        # 统计 [L, R] 区间内字符 c 的数量
        cnt = 0
        for i in range(L, R + 1):
            if S[i] == c:
                cnt += 1
        if cnt >= x:
            ans += 1
    print(ans)