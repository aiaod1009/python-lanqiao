n,m  = map(int,input().split())
a = list(map(int,input().split()))
a = sorted(set(a))

vis = [False] * (n + 2)# 标记数组：vis[x] = True 表示第 x 个灯塔亮了
ans = 0

for x in a:
    if not vis[x-1] and not vis[x+1] and not vis[x]:
        ans += 1
        vis[x] = True
print(ans)

# 去重:同一个灯塔被尝试多次，只需要记一次（多次尝试等价于一次）。
# 排序:把所有被尝试过的灯塔按编号从小到大排好。
# 贪心点亮:从左到右遍历，只要这个灯塔的「左、右、自己」都没亮，就点亮。