n = int(input().strip())
a = [0]+list(map(int,input().split()))
a.sort()
x = 0
for i in range(1,n+1):
    if i % 2 != 0:
        x += a[i]
    else:
        x -= a[i]
print(x)
