#1 暴力枚举
# def find_i(i):
#     a = i.find('2')
#     if a == -1:
#         return 0
#     b = i.find('0',a+1)
#     if b == -1:
#         return 0
#     c = i.find('2', b + 1)
#     if c == -1:
#         return 0
#     d = i.find('3', c + 1)
#     if d == -1:
#         return 0
#     return 1
# cnt = 0
# for i in range(12345678,98765433):
#     if find_i(str(i)) == 0:
#         cnt += 1
# print(cnt)

# 2 枚举
# max_cnt = [0] * 4046
# for i in range(1,2023):
#     max_cnt[i] += i
#
# for i in range(1,2023):
#     for j in range(i+1,2023):
#         s = i + j
#         add = min(i,j)
#         max_cnt[s] += add
# print(max(max_cnt))

# 3 线性二维dp
import sys
input = lambda: sys.stdin.readline().strip()
s = input()
n = len(s)
dp = [[0]*2 for _ in range(n+1)]
def val(c):
    return ord(c)-96
# dp[0][0]=0
# dp[0][1]=val(s[0])
for i in range(1,n+1):
    dp[i][0] = max(dp[i-1][0],dp[i-1][1])
    dp[i][1] = dp[i-1][0] + val(s[i-1])
print(max(dp[n][0],dp[n][1]))














