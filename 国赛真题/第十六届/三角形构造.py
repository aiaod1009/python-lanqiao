x = int(input().strip())
ans = 0
for y in range(1, x + 1):
    # 题目给的三个三角形条件，等价于我们算出来的 x + y > (x | y)
    if x + y > (x | y):
        ans += 1
print(ans)