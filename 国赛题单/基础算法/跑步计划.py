m=[0,31,28,31,30,31,30,31,31,30,31,30,31]
day=7
ans=0
for i in range(1,13):
    for j in range(1,m[i]+1):
        if i in [11,12,1] or j==1 or (10<=j<20) or j in [21,31] or day % 7==1 or i==10:
            ans += 5
        else:
            ans += 1
        day += 1
print(ans)