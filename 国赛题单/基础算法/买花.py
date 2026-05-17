n,k=map(int,input().split())
s = input().strip()
#前缀和
pre = [[0] * 26]
for i in range(n):
    pre.append(pre[-1].copy())
    pre[-1][ord(s[i])-ord('a')] += 1
ans = 0
for i in range(n-k+1):
    for j in range(i+k,i+k*26+1,k):
        if j > len(pre):
            break
        f = 1
        for s in range(26):
            cnt = pre[j][s] - pre[i][s]
            if cnt > k:
                f = -1
                break
            elif 0 < cnt < k:
                f = 0
                break
        if f == 1:
            ans += 1
        elif f == -1:
            break
print(ans)


#只能过50%  暴力
# ans = 0
# for i in range(n):
#     c = [0] * 26
#     for j in range(i,n):
#         x=ord(s[i])-ord('a')
#         c[x]+=1
#         if c[x]>k:
#             break
#         if all(v==0 or v == k for v in c):
#             ans += 1
# print(ans)