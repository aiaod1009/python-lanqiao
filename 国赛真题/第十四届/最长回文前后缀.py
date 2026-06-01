def ifhuiwen(s):
    return s == s[::-1]
s = input().strip()
n = len(s)
ml = 0
#前缀和后缀可以重叠
for i in range(n+1):
    for j in range(n+1):
        pre = s[:i]
        suf = s[n-j:]
        c = pre + suf
        if ifhuiwen(c):
            ml = max(ml,len(c))
print(ml)