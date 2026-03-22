n,m = map(int,input().split())
s = input().strip()
t = input().strip()
cnt = 0
for i in range(n):
    if s[i] == t[i]:
        cnt += 1
print(n - abs(cnt - m))

#相同题数 ≤ 朋友答对题数
#cnt + n - m
#相同题数 > 朋友答对题数
#m + n - cnt