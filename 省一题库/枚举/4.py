a = [i**3 for i in range(1,2026)]
ans=0
for i in a:
    if int(str(i)[-1]) == 3:
        ans += 1
print(ans)