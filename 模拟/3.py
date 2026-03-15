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
    x = 0
    ans = ''.join(reversed(str(N)[1:]))
    for i in range(len(ans)):
        if ans[i] != '0':
            x = i
            break
    print('-'+ans[x:])
else:
    print(0)