n = int(input())
a = list(map(int, input().split()))

# 统计每个 id 出现次数
cnt = {}
for x in a:
    cnt[x] = cnt.get(x, 0) + 1

ans1 = 0  # 多余的人数（>=2 的 id 中需要改的人数）
ans2 = 0  # 孤立的人数（==1 的 id 的人数）

for v in cnt.values():
    if v >= 2:
        ans1 += v - 2
    else:  # v == 1
        ans2 += 1

if ans1 >= ans2:
    print(ans1)
else:
    print(ans1 + (ans2 - ans1) // 2)