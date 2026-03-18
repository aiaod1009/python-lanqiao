a = [i**3 for i in range(1,2026)]
ans=0
for i in a:
    if int(str(i)[-1]) == 3:
        ans += 1
print(ans)

#数学法
count = 0
for i in range(1, 2026):
    if i % 10 == 7:
        count += 1
print(count)  # 结果也是 202