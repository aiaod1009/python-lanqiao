# 暴力代码
# n,c = map(int,input().split())
# s = list(map(int,input().split()))
# ans = 0
# for j in range(n):
#     for i in range(n):
#         if s[i] - s[j] == c:
#             ans += 1
# print(ans)

#哈希做法(等价于 A=B+C)
n, c = map(int, input().split())
ab = list(map(int, input().split()))
count = {}
for i in ab:
    if i in count:
        count[i] += 1
    else:
        count[i] = 1
ans = 0
for b in ab:
    #两种方法都可以
    # if b + c in count:
    # ans += count[b+c]
    ans += count.get(b+c,0)
print(ans)