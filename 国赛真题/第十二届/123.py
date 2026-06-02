import sys
input = lambda:sys.stdin.readline().strip()
pre = [0]
num = 1 # 当前是第num组：1~num
cnt = 0
while len(pre) <= 1000010:
    for i in range(1,num+1):
        pre.append(pre[-1]+i)
    num += 1
t = int(input())
for _ in range(t):
    l,r = map(int,input().split())
    print(pre[r] - pre[l-1])