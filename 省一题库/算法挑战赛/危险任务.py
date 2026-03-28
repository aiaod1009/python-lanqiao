#以为使用dfs，没想到是用贪心，因为数据太大了
a, b, c = map(int, input().split())
res = 0
while a < b:
    # 尽量走+2，但要检查下一个位置是否危险
    if a + 2 <= b and (a + 2) % c != 0:
        a += 2
    else:
        a += 1
    res += 1

print(res)