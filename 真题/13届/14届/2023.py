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

# 3 线性二维dp(一维也可以解，详细看2023-3）
# import sys
# input = lambda: sys.stdin.readline().strip()
# s = input()
# n = len(s)
# dp = [[0]*2 for _ in range(n+1)]
# def val(c):
#     return ord(c)-96
# # dp[0][0]=0
# # dp[0][1]=val(s[0])
# for i in range(1,n+1):
#     dp[i][0] = max(dp[i-1][0],dp[i-1][1])
#     dp[i][1] = dp[i-1][0] + val(s[i-1])
# print(max(dp[n][0],dp[n][1]))

# 4 贪心+二分






# 5 二维线性dp(偏难)
# import sys
# input = lambda: sys.stdin.readline().strip()
# n = input()
# x = input()
# y = input()



# 6 树形DP
import sys
input = lambda: sys.stdin.readline().strip()
n = int(input())
fa = [0, 0] + list(map(int, input().split()))
v = [0] + list(map(int, input().split()))  # 存1~n个结点的值
dep = [0] * (n + 1)  # 每个结点的深度
dep_node = [[] for i in range(n + 1)]  # 存每个深度中的结点编号
deep_max = 0  # 深度的最大值

for i in range(1, n + 1):  # 求每个深度有哪些结点
    dep[i] = dep[fa[i]] + 1
    deep_max = max(deep_max, dep[i])
    dep_node[dep[i]].append(i)

dp = [[0] * 2 for i in range(n + 1)]  # 表示i结点选或不选的情况dp[i][0/1]

state = [0, 0, 0]  # [不选该层结点的最大值结点,选该层结点的最大值结点,选该层结点非最大值同父最大值结点]
for i in range(deep_max, 0, -1):  # 从deep_max~1深度,自下向上
    for j in dep_node[i]:  # j表示i深度的结点
        dp[j][0] = max(dp[state[0]][0], dp[state[1]][1])
        if fa[state[1]] == j:  # 如果下一层的最大值结点是j的子结点, 则选择max(非j子结点的最大值, 不选的最大值结点)
            dp[j][1] = v[j] + max(dp[state[0]][0], dp[state[2]][1])
        else:  # max(下一层的最大值结点, 不选的最大值结点)
            dp[j][1] = v[j] + max(dp[state[0]][0], dp[state[1]][1])

    state = [0, 0, 0]
    for j in dep_node[i]:  # 求深度为i的dp[j][0]和dp[j][1]的最大值
        if dp[state[0]][0] < dp[j][0]:state[0] = j
        if dp[state[1]][1] < dp[j][1]:state[1] = j

    for j in dep_node[i]:  # 求i深度下和选最大值结点非共同父结点的次最大值结点
        if fa[state[1]] != fa[j] and dp[state[2]][1] < dp[j][1]:
            state[2] = j

print(max(dp[1][0], dp[1][1]))


# 8 图论 树 贪心





# 9 树



# 10 模拟+贪心
# import sys
# input = lambda: sys.stdin.readline().strip()
# n = int(input())
# arr = list(map(int,input()))
# for i in range()



























