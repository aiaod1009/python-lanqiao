#10%暴力分数
import itertools
# 1. 读入全部数据
n = int(input())
strings = [input().strip() for _ in range(n)]
# 2. 依次处理前 i 个字符串
for i in range(1, n + 1):
    current = strings[:i]  # 截取前 i 个串
    max_owo = 0
    # 3. 试遍所有拼接顺序
    for p in itertools.permutations(current):
        joined = "".join(p)  # 拼成大字符串
        # 4. 从头到尾遍历数 owo（允许重叠）
        cnt = 0
        for idx in range(len(joined) - 2):
            if joined[idx: idx + 3] == "owo":
                cnt += 1
        # 5. 记录最高得分
        if cnt > max_owo:
            max_owo = cnt
    print(max_owo)