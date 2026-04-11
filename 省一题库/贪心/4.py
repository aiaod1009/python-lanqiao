k = int(input().strip())
s = input().strip()
if len(s) % k != 0:
    print(-1)
else:
    cnt = 0
    m = len(s) // k
    for i in range(m):
        c = [0] * 26  #字母出现次数
        for j in range(i, len(s), m):
            c[ord(s[j]) - 97] += 1
        cnt += k - max(c)  #改成出现最多的那个字母的次数
    print(cnt)
