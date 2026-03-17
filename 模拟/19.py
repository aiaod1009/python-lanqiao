h,w = map(int,input().split())
s = 'LANQIAO' * (h+w)
x = []
for i in range(h):
    x.append(s[i:w+i])
cnt = 0
for i in range(h):
    for j in range(w):
        if x[i][j] == 'A':
            cnt += 1
print(cnt)

#数学取模
h, w = map(int, input().split())
s = "LANQIAO"
res = 0
for i in range(h):
    for j in range(w):
        if s[(i + j) % 7] == 'A':
            res += 1
print(res)