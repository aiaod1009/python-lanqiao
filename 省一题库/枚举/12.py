n = int(input())
l1 = list(map(int,input().split()))
l2 = list(map(int,input().split()))
def check(x):
    while x:
        if x % 10 in (2,4,0):
            return True
        x //= 10
    return False
c = 1
cnt = 0
for i in range(n):
    if c % 2 != 0:
        if check(l1[i]):
            cnt += 1
            c += 1
    else:
        if check(l2[i]):
            cnt += 1
            c += 1
print(cnt)