import sys
input = lambda:sys.stdin.readline().strip()
n = int(input())
x = sorted(int(input()) for _ in range(n))
y = sorted(int(input()) for _ in range(n))
c = 0
for i in range(n):
    c += abs(x[i]-y[i])
print(c)