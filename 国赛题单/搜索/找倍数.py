from collections import deque
n = int(input().strip())
vis = [False] * n
q = deque()
q.append((1 % n,"1")) # 起点：数字1，余数是1%n，字符串是"1"
while q:
    r,s = q.popleft()
    if r == 0:
        print(s)
        break
    nr = (r*10) % n
    if not vis[nr]:
        vis[nr] = True
        q.append((nr,s+"0"))
    nr  = (r*10+1) % n
    if not vis[nr]:
        vis[nr] = True
        q.append((nr,s+"1"))

