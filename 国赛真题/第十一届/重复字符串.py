k = int(input().strip())
s = input().strip()
n = len(s)
if n % k != 0:
    print(-1)
else:
    l = n // k
    res = 0
    for i in range(l):
        # g = s[i::l]
        cnt = [0] * 26
        for j in range(k):
        # for c in g:
            c = s[i + j*l]
            cnt[ord(c)-ord('a')] += 1
        res += k - max(cnt)
    print(res)