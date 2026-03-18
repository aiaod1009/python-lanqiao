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