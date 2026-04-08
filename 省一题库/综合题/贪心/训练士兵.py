import sys
input=lambda:sys.stdin.readline().strip()
n,s = map(int,input().split())
# nums = [[0,0] for _ in range(n)]
nums = [list(map(int, input().split())) for _ in range(n))]
p,c = [0] * n,[0] *n
# for i in range(n):
    # nums[i] = list(map(int,input().split()))
nums.sort(key=lambda x:x[1]) # 按升序
for i in range(n):
    p[i],c[i] = nums[i][0],nums[i][1]
res = cnt = 0
tot = sum(p)
for i in range(n):
    if tot >= s:
        res += (c[i] - cnt) * s
        cnt = c[i]
    else:
        res += (c[i] - cnt) * p[i]
    tot -= p[i]
print(res)