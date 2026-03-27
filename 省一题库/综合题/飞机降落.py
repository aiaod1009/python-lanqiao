import math
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True
def dfs(start, count, current_sum):
    global ans
    if count == k:
        if is_prime(current_sum):
            ans += 1
        return
    for i in range(start, n):
        dfs(i + 1, count + 1, current_sum + nums[i])
# 输入处理
n, k = map(int, input().split())
nums = list(map(int, input().split()))
ans = 0
dfs(0, 0, 0)
print(ans)