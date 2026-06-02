#贪心：总耗时（s+a+e）小的人靠前，让小的e去拖累后面
#大的e尽量靠后少拖累人，总和自然最小
n = int(input())
stu = []
for _ in range(n):
    s,a,e = map(int,input().split())
    key = s+a+e
    stu.append((key,s,a,e))
# 贪心：按key升序
stu.sort()
pre = 0
ans = 0
for k,s,a,e in stu:
    now = pre + s + a
    ans += now
    pre = now + e
print(ans)
