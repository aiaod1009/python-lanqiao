n = int(input().strip())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
C = list(map(int,input().split()))

def pd(a2,b2,c2):
    #zip 把 “第1个列表的第i个元素、第2个列表的第i个元素、第3个列表
    #的第i个元素” 打包成一个元组，遍历同时拿到三个列表的同位置元素
    js = [a-b-c for a,b,c in zip(a2,b2,c2)]
    js.sort(reverse=True)  #逆序从大到小排序
    res = 0  # 记录最多能发生的事件数
    k = 0    # 记录当前选中事件的「总净收益」（即 X-Y-Z 的总和）
    for i in range(n):
        k += js[i]  # 把第i+1个事件的净收益加进去
        if k > 0:
            res = i + 1
        else:
            break
    return res
x = pd(A,B,C)
y = pd(B,A,C)
z = pd(C,A,B)
print(-1 if max(x,y,z) == 0 else max(x,y,z))