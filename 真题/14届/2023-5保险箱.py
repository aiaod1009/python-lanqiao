import sys
import math


def main():
    # 1. 读取输入
    n = int(sys.stdin.readline().strip())
    x_str = sys.stdin.readline().strip()
    y_str = sys.stdin.readline().strip()

    # 2. 拆位、转int、反转
    x = list(map(int, reversed(x_str)))
    y = list(map(int, reversed(y_str)))

    # 3. 初始化DP表
    INF = math.inf
    dp = [[INF] * 3 for _ in range(n + 1)]
    dp[0][1] = 0  # 初始状态：无进位，次数0

    # 4. 动态规划核心逻辑
    for i in range(1, n + 1):
        xi = x[i - 1]
        yi = y[i - 1]

        for c_prev in [-1, 0, 1]:
            if dp[i - 1][c_prev + 1] == INF:
                continue

            current = xi + c_prev
            for c_curr in [-1, 0, 1]:
                delta = yi + 10 * c_curr - current
                new_cost = dp[i - 1][c_prev + 1] + abs(delta)
                if new_cost < dp[i][c_curr + 1]:
                    dp[i][c_curr + 1] = new_cost

    # 5. 输出结果（兼容单一位/多位场景）
    if n == 1:
        # 单一位：最高位进退位忽略，取所有状态的最小值
        result = min(dp[1][0], dp[1][1], dp[1][2])
    else:
        # 多位：最高位不能有进退位，取无进位状态
        result = dp[n][1]

    print(result)


if __name__ == "__main__":
    main()


# import sys
# n = int(input())
# s1 = input()[::-1]
# s2 = input()[::-1]
# #字符串反转后第一位是个位，第二位是十位...
# a = [0]
# b = [0]
# for i in range(n):
#     a.append(int(s1[i]))
#     b.append(int(s2[i]))
# dp = [[sys.maxsize]*3 for i in range(n+1)]
# dp[1][0] = abs(a[1]-b[1])#不进退直接加减
# dp[1][1] = 10-a[1]+b[1]#a[1]进位到b[1]
# dp[1][2] = 10+a[1]-b[1]#a[1]退位到b[1]
# for i in range(2,n+1):
#     dp[i][0] = min(dp[i-1][0]+abs(a[i]-b[i]),dp[i-1][1]+abs(a[i]+1-b[i]),dp[i-1][2]+abs(a[i]-1-b[i]))
# #上一位不进退直接加减后这一位也直接加减;上一位进位后这一位多个1,然后直接加减;上一位退位后这一位少个1,然后直接加减。取最小值为直接加减次数
#     dp[i][1] = min(dp[i-1][0]+10-a[i]+b[i],dp[i-1][1]+9-a[i]+b[i],dp[i-1][2]+11-a[i]+b[i])
# #上一位不进退直接加减这一位进位;上一位进位后这一位进位;上一位退位后这一位进位。取最小值为进位次数
#     dp[i][2] = min(dp[i-1][0]+10+a[i]-b[i],dp[i-1][1]+11+a[i]-b[i],dp[i-1][2]+9+a[i]-b[i])
# #上一位不进退直接加减这一位进位;上一位进位后这一位退位;上一位退位后这一位退位。取最小值为退位次数
# ans = min(dp[n][0],dp[n][1],dp[n][2])#取三者最小值即为答案
# #例如从49到21，先看个位9到1，有三种情况，
# #第一种是不进退直接加减，操作次数为9-1=8;
# #第二种是9进位到1，操作次数为10-9+1=2;
# #第三种是9退位到1，操作次数是10+9-1=18
# #然后看十位4到2，也有三种情况同上，这时要看上一位是否进退位，以第一种情况为例
# #如果不进位直接加减，操作次数为4-2=2;如果上一位进位9+2=11，个位为1，十位会多个1，所以是5到2而不是4到2，操作次数加1，退位同理，是3到2而不是4到2，操作次数减1
# #后面同理
# print(ans)