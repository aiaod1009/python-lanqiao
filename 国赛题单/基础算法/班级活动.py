n = int(input().strip())
a = [0]+list(map(int,input().split()))
num = [0 for i in range(n+1)]
cnt = 0
for j in a[1:]:
    num[j] += 1
s1,s2 = 0,0
for x in num:
    if x == 0:
        continue
    if x == 1:
        s2 += 1
    elif x >= 2:
        s1 += x - 2
if s1 > s2:
    print(s1)
else:
    print(s1 + (s2 - s1)//2)