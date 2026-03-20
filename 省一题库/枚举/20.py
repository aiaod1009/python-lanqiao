# import math
# ans = 0
# for a in range(1, 1000001):
#     for b in range(a + (2025 - 2 * a % 2025), 1000001, 2025):
#         if math.gcd(a, b) == 1:
#             ans += 1
# print(ans)

#解释第四行
# 核心等式：(a+b)%2025==0 → b=2025k -a；
# 加上 b>a 条件后，最小的 b 就是 a + (2025 - 2a%2025)；
# 步长取 2025，是因为 b+2025 后，a+(b+2025) 还是 2025 的倍数。


import math
ans = 0
m = 10**6
for a in range(1, m + 1):
    # 第一步：算最小的k（满足 2025k > 2a）
    k = math.ceil((2*a) / 2025)
    b = 2025 * k - a
    # 第三步：遍历所有合法的b（步长2025）
    for b_val in range(b, m + 1, 2025):
        if math.gcd(a, b_val) == 1:
            ans += 1
print(ans)




# import math
# ans = 0
# m = 10 ** 6
# # 枚举 a+b = sum（sum是2025的倍数），sum最大为 2*1e6（a和b都≤1e6）
# for s in range(2025, 2 * m + 1, 2025):
#     a_start = max(1, s - m)
#     a_end = min(s // 2 - 1, m)
# 
#     for a in range(a_start, a_end + 1):
#         b = s - a
#         if b > m:
#             continue
#         if math.gcd(a, b) == 1:
#             ans += 1
# print(ans)