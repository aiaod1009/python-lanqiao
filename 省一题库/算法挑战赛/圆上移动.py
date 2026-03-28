n,m,x = map(int,input().split())
a = list(map(int,input().split()))
cnt = 0
for i in a:
    if i > 0:
        x += i
        if x % m == 0:
            cnt += 1
    elif i < 0:
        x += i
        if x % m == 0:
            cnt += 1
    else:
        if x % m == 0:
            cnt += 1
print(cnt)

n, m, x = map(int, input().split())
a = list(map(int, input().split()))
cnt = 0
for num in a:
    x += num  # 直接加，正负自动处理方向
    if x % m == 0:
        cnt += 1
print(cnt)