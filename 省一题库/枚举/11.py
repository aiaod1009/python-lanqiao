#很暴力的方法，只有二十分
# k = int(input())
# s,c1,c2 = input().split()
# s = list(s)
# ans = 0
# for i in range(len(s)):
#     if s[i] == c1:
#         for j in range(i+k-1,len(s)):
#             if s[j] == c2:
#                 ans += 1
# print(ans)

#前缀和
k = int(input())
s,c1,c2 = input().split()
n = len(s)
ans = 0

pre = [0] * (n + 1)  #用一个额外的位置（pre [0]）做「兜底基准」
for i in range(n):     #pre[i]表示前面有几个c2
    pre[i+1] = pre[i] + (1 if s[i] == c2 else 0)

for i in range(n):
    if s[i] == c1:
        min_j = i + k -1
        if min_j >= n:
            continue
        ans += pre[n] - pre[min_j] #n到k有几个c2
print(ans)

# 双指针写法
K = int(input())
S,c1,c2 = input().split()
n = len(S)
ans = 0
cnt = 0
# i从0开始，j从K-1开始，同步右移
i, j = 0, K - 1
while j < n:
    if S[i] == c1:
        cnt += 1   #左边有多少个c1
    if S[j] == c2:
        ans += cnt  #遇到c2，答案就可以加上多少个
    i += 1
    j += 1

print(ans)




