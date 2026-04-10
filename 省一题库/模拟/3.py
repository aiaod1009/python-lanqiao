N=int(input())
if N > 0:
    y = 0
    ans = ''.join(reversed(str(N)))
    for i in range(len(ans)):
        if ans[i] != '0':
            y = i
            break
    print(ans[y:])
elif N < 0:
    # ans = ''.join(reversed(str(N)[1:]))
    ans = str(N)[1:][::-1].lstrip('0')
    print('-'+ans)
else:
    print(0)

#简单写法
# s = input().strip()
# if s == '0':
#     print(0)
# elif s.startswith('-'):
#     rev = s[1:][::-1].lstrip('0')
#     print('-' + rev)
# else:
#     rev = s[::-1].lstrip('0')
#     print(rev)

N = int(input())
# 处理0的特殊情况
if N == 0:
    print(0)
else:
    # 记录符号，统一转正数处理
    sign = 1
    if N < 0:
        sign = -1
        N = -N
    res = 0
    while N > 0:
        # 取最后一位
        digit = N % 10
        # 把当前位放到结果的末尾
        res = res * 10 + digit
        # 去掉最后一位
        N = N // 10
    # 还原符号
    print(sign * res)