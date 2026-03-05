import os
import sys

# 请在此输入您的代码
result = [0 for _ in range(4047)]
for i in range(1, 2023):
    result[i] = i

for i in range(2, 2023):
    result[i * 2] += i // 2

for i in range(1, 2024):
    for j in range(i + 1, 2024):
        result[i + j] += i
print(max(result))