max_sum = 0
best_x = 0

# 我们只需要检查 x 在 [2, 4046] 这个范围内，因为最大的兑换面值是 2023 + 2023 = 4046
for x in range(2, 4047):
    current_sum = 0
    # 初始数量
    if x <= 2023:
        current_sum += x
    # 旧版贡献
    for a in range(1, x):
        b = x - a
        if 1 <= a <= 2023 and 1 <= b <= 2023:
            current_sum += min(a, b)
    if current_sum > max_sum:
        max_sum = current_sum
        best_x = x

print(max_sum)
# print(f"对应的面值 x: {best_x}")