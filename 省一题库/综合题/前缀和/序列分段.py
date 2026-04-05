import sys
input=lambda:sys.stdin.readline().strip()
t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    s=sum(a)
    # 计算所有后缀和
    # 每切 1 刀，总价值的增量 = 切分位置后面所有数的和（后缀和）
    cur=0
    suf=[] # 后缀和
    for num in reversed(a): # 从数组末尾往前遍历，依次累加
        cur+=num
        suf.append(cur)
    suf=suf[:-1] #切片去掉最后一个元素（最后一个元素是数组总和，不是切分增量）
    suf.sort(reverse=True) #降序排序后缀和，保证每次选最大的增量（贪心）
    res=[s] #第一个元素是k=1的答案（总和s）
    for x in suf:
        s+=x
        res.append(s)
    print(*res)