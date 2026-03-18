import os
import sys

# from collections import Counter
# # 请在此输入您的代码

# s=sys.stdin.readline().strip()

# count = Counter(s)

# for c in count:
#   if count[c] % 2 != 0:
#     print("NO")
#     exit()

# print("YES")


# n = input()
# n_ = set(n)
# for i in n_:
#   if n.count(i)%2==0:
#     result = "YES"
#     continue
#   else:
#     result = "NO"
#     break
# print(result)


ans = 0
for i in input():
    ans ^= ord(i)
print("NO" if ans else "YES")