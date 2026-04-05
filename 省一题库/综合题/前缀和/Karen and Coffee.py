import sys
input = lambda:sys.stdin.readline().strip()
n,k,q = map(int,input().split())
max_temp = 200000
# 差分数组
diff = [0] * (max_temp + 2)
for _ in range(n):
    l, r = map(int, input().split())
    diff[l] += 1
    diff[r + 1] -= 1
sum1 = 0  # 当前温度被推荐次数
sum2 = 0  # 到当前为止可接受温度总数
pre = [0] * (max_temp + 1)
for x in range(1, max_temp + 1):
    sum1 += diff[x]
    if sum1 >= k:
        sum2 += 1 # 可接受的+1
    pre[x] = sum2 #到 x 为止，有几个可接受温度
for _ in range(q):
    a, b = map(int, input().split())
    print(pre[b] - pre[a - 1])