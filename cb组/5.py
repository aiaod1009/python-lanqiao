def countLQ(s):
    res, L = 0, 0
    for c in s:
        if c == 'L':
            L += 1
        if c == 'Q':
            res += L
    return res

max_ans = 0
n = int(input())
s = input().strip()

def dfs(pos, now):
    global max_ans
    if pos == n:
        max_ans = max(max_ans, countLQ(now))
        return
    if s[pos] != '?':
        dfs(pos+1, now+s[pos])
    else:
        dfs(pos+1, now+'L')
        dfs(pos+1, now+'Q')

dfs(0, "")
print(max_ans)

n = int(input())
s = input().strip()

# 先统计总Q数量（所有Q+?）
total_q = sum(1 for c in s if c in ('Q', '?'))
pre_l = 0
max_ans = 0

for c in s:
    # 遍历当前字符，把它算进L，总Q里减去它（因为它不再是Q了）
    if c in ('L', '?'):
        pre_l += 1
    if c in ('Q', '?'):
        total_q -= 1
    # 计算当前分割点的聚合数
    max_ans = max(max_ans, pre_l * total_q)

print(max_ans)