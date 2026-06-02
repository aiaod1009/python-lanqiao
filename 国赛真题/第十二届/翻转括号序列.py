n, m = map(int, input().split())
s = list(input().strip())
for _ in range(m):
    query = input().split()
    op = int(query[0])
    if op == 1:
        l = int(query[1]) - 1
        r = int(query[2]) - 1
        for i in range(l, r + 1):
            s[i] = ')' if s[i] == '(' else '('
    else:
        l = int(query[1]) - 1
        score = 0
        max_r = 0
        for r in range(l, n):
            score += 1 if s[r] == '(' else -1
            if score < 0:  # 爆掉了，直接掐断
                break
            if score == 0: # 完美配对，记录当前 1-based 位置
                max_r = r + 1
        print(max_r)