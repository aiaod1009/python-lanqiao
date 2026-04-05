from collections import deque
import sys
d = {'E':(0,1),'S':(1,0),'W':(0,-1),'N':(-1,0)}
for line in sys.stdin:
    n = int(line)
    if n == 0:
        break
    s = sys.stdin.readline().strip()

    q = deque((25,i) for i in range(11,31))
    err,step=0,0
    for c in s:
        step += 1
        x,y = q[-1]
        nx,ny = x+d[c][0],y+d[c][1]  #根据方向 c 计算新头部的坐标
        if nx < 1 or nx>50 or ny < 1 or ny > 50:
            err=2
            break
        # 撞自己判断
        t = q.copy()
        t.popleft()
        t.append((nx,ny))
        if len(t) != len(set(t)): #如果长度和原列表 t 不同，说明有坐标重复
            err = 1
            break
        # 合法再真正移动
        q.popleft()
        q.append((nx,ny))

    if err == 1:
        print(f"The worm ran into itself on move {step}.")
    elif err==2:
        print(f"The worm ran off the board on move {step}.")
    else:
        print(f"The worm successfully made all {step} moves.")
