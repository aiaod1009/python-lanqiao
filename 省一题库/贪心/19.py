import sys
input=lambda :sys.stdin.readline().strip()
n = int(input())
t = n // 10
c = [[] for _ in range(10)]
for _ in range(n):
    a,b = map(int,input().split())
    c[a].append(b)
s = 0
for x in range(10):
    l = sorted(c[x])
              #多出来了多少个数字(正/负)
    s += sum(l[:len(l) - t]) if len(l) > t else 0
print(s)

#不用写 “补” 的代码!!!!删的过程，就是补的过程，代价只算一次 ✅