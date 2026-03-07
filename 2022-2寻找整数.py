import math

# 把抄好的数字直接放这里
r_tuple = (
    1, 2, 1, 4, 5, 4, 1, 2, 9, 0, 5, 10, 11, 14, 9, 0, 11, 18, 9, 11,
    11, 23, 17, 9, 23, 20, 25, 16, 29, 27, 25, 11, 17, 4, 29, 22,
    37, 23, 9, 1, 11, 11, 33, 29, 15, 5, 41, 46
)

current = r_tuple[0]  # a=2 的余数
step = 2

for i in range(1, len(r_tuple)):
    a = i + 2  # 下标i对应除数a=i+2
    target_r = r_tuple[i]
    while current % a != target_r:
        current += step
    step = step * a // math.gcd(step, a)

print(current)