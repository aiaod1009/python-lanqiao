N = list(map(int,input().split()))
n = N[0]
a = N[1:]
ans = set()
if n == 1:
    print('Jolly')
else:
    for i in range(1, n):
        ans.add(abs(a[i] - a[i - 1]))
    if ans == set(range(1,n)):
        print('Jolly')
    else:
        print('Not jolly')
