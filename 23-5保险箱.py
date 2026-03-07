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