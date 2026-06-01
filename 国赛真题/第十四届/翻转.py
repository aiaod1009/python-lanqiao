n = int(input())
arr = [input() for _ in range(n)]
min_total = 999999
# 总共有 2^n 种组合，循环每一种
total_case = 2 ** n
for case in range(total_case):
    # 先构造当前这一组的字符串
    now = []
    temp = case
    for s in arr:
        # temp 奇偶判断：0不反转，1反转
        if temp % 2 == 1:
            now.append(s[::-1])
        else:
            now.append(s)
        temp = temp // 2  # 看下一位
    # 计算当前组合的拼接长度
    res = 2
    last_char = now[0][1]
    for i in range(1, n):
        if now[i][0] == last_char:
            res += 1
        else:
            res += 2
        last_char = now[i][1]
    if res < min_total:
        min_total = res
print(min_total)