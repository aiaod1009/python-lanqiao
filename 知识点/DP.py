#记忆化搜索
from functools import *  # 导入 lru_cache 等工具
class Solution:
    def climbStairs(self, n: int) -> int:
        @lru_cache(maxsize = None)  # 给 dfs 加上记忆化缓存
        def dfs(n):
            # 边界条件：n=0 或 n=1 时，只有 1 种方法
            return 1 if n == 1 or n == 0 else dfs(n - 1) + dfs(n - 2)
        return dfs(n)  # 调用带缓存的 dfs

s = Solution()
print(s.climbStairs(3))  # 输出 3

# @lru_cache(maxsize=None)
# def dfs(n):
#     if n == 0 or n == 1:
#         return 1
#     return dfs(n-1) + dfs(n-2)
#
# n = int(input())
# print(dfs(n))

# @lru_cache
# def dfs(n):
#     if n == 1:
#         return 1  # 爬1阶：只有1种
#     if n == 2:
#         return 2  # 爬2阶：1+1 / 2，共2种
#     return dfs(n-1) + dfs(n-2)
#
# print(dfs(3))  # 3，和原代码结果一致

# 无typing版
def rob(nums):
    n = len(nums)
    f = [[0] * 2 for _ in range(n + 1)]
    for i in range(1, n + 1):
        f[i][0] = max(f[i-1][1], f[i-1][0])
        f[i][1] = f[i-1][0] + nums[i-1]
    return max(f[n][1], f[n][0])

nums = [1,2,3,1]
print(rob(nums))  # 输出4，完全正常