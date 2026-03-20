import sys
input = lambda :sys.stdin.readline().strip()
n = int(input())
ptr = 1
for _ in range(n):
    s = input()
    ptr += 1
    upper = lower = digit = cnt_O = cnt_o = cnt_0 = 0
    for c in s:
        if c == 'O':
            cnt_O += 1
        elif c == 'o':
            cnt_o += 1
        elif c == '0':
            cnt_0 += 1
        elif c.isupper():
            upper += 1
        elif c.islower():
            lower += 1
        elif c.isdigit():
            digit += 1
    # 2. 已满足三种类型,都大于0 → 输出0
    if (upper + cnt_O) and (lower + cnt_o) and (digit + cnt_0):
        print(0)
        continue
    # 3. 尝试用O/o/0补全缺失类型
    if not upper and cnt_O: upper, cnt_O = 1, cnt_O - 1
    if not lower and cnt_o: lower, cnt_o = 1, cnt_o - 1
    if not digit and cnt_0: digit, cnt_0 = 1, cnt_0 - 1
    # 4. 计算缺失类型数 + 输出结果
    missing = sum([not (upper + cnt_O), not (lower + cnt_o), not (digit + cnt_0)])
    total = cnt_O + cnt_o + cnt_0
    print(missing if total >= missing else -1)