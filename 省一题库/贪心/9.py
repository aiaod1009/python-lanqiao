n = int(input())
a = [0]+list(map(int,input().split()))
res = 0
for i in range(1,n+1):
    while a[i] != i:
        tmp = a[a[i]]
        a[a[i]] = a[i]
        a[i] = tmp
        res += 1
print(res)