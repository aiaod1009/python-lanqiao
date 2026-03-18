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