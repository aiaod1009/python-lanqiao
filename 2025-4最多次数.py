#贪心算法
import sys

s = sys.stdin.readline().strip()
n = len(s)
count = 0
i = 0

while i <= n - 3:
    substr = s[i:i+3]
    if set(substr) == {'l', 'q', 'b'}:
        count += 1
        # 贪心核心：找到第一个有效三元组，立即切割，直接跳3步（不回头）
        i += 3
    else:
        # 没找到就往后挪1步，继续找下一个可能的三元组
        i += 1

print(count)