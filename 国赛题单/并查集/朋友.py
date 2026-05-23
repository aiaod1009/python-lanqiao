import sys
input = lambda:sys.stdin.readline().strip()
n,m,p,q = map(int,input().split())
fa_man = list(range(n + 1))
sz_man = [1] * (n + 1)

fa_woman = list(range(m + 1))
sz_woman = [1] * (m + 1)

def find(x, fa):
    if fa[x] != x:
        fa[x] = find(fa[x], fa)
    return fa[x]
def union(u, v, fa, sz):
    ru, rv = find(u, fa), find(v, fa)
    if ru != rv:
        fa[ru] = rv
        sz[rv] += sz[ru]

for _ in range(p):
    x1,y1 = map(int,input().split())
    union(x1, y1, fa_man, sz_man)
for _ in range(q):
    x2,y2 = map(int,input().split())
    union(abs(x2), abs(y2), fa_woman, sz_woman)

ans_man = sz_man[find(1, fa_man)]
ans_woman = sz_woman[find(1, fa_woman)]
print(min(ans_man, ans_woman))