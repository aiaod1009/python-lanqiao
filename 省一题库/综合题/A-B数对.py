# 暴力代码
# n,c = map(int,input().split())
# s = list(map(int,input().split()))
# ans = 0
# for j in range(n):
#     for i in range(n):
#         if s[i] - s[j] == c:
#             ans += 1
# print(ans)

#哈希做法
from collections import defaultdict

n, c = map(int, input().split())
s = list(map(int, input().split()))

# 1. 预处理：把所有数字出现的次数统计起来
# key是数字值，value是这个值出现的次数
count = defaultdict(int)
for num in s:
    count[num] += 1

ans = 0

# 2. 遍历每一个 B，寻找有多少个 A = B + C
for b in s:
    a = b + c
    # 如果A存在，加上A出现的次数
    ans += count.get(a, 0)
print(ans)