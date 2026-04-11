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