sticks = [6,2,5,5,4,5,6,3,7,6]
def solve(n):
    if n < 2:
        return -1
    k = 1   # 满足条件的最小位数
    while True:
        if 2*k <= n <= 7*k:
            break
        k += 1
    res = []
    rem = n
    # 经确定好 k 之后，开始逐位构造数字
    for i in range(k):
        s = 1 if i==0 else 0  #「当前位可以尝试的最小数字」
        for d in range(s,10):
            c = sticks[d]
            left = k-i-1 # 拼完当前这一位后，还剩下几位数要拼
            # 如果这个数字 d 能用 → 选中，break，不再试后面的数字
            if c<=rem and 2*left <= rem-c <= 7*left:
                res.append(str(d))
                rem -= c
                break
    return ''.join(res)
t = int(input())
for _ in range(t):
    n = int(input())
    print(solve(n))