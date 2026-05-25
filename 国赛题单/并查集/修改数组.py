import sys
input = lambda:sys.stdin.readline().strip()
n = int(input())
a = list(map(int,input().split()))
fa = {}
def find(x):
    if x not in fa:
        return x
    fa[x] = find(fa[x])
    return fa[x]
ans = []
for x in a:
    pos = find(x)
    ans.append(pos)
    fa[pos] = pos + 1
print(*ans)