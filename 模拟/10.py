import sys
input = lambda :sys.stdin.readline().strip()
d = [list(input().split()) for i in range(2000)]
k = 0
curr_k = 0
last = None
for i in range(2000):
    if d[i][0] == d[i][1]:
        time=int(d[i][2])
        if last is None:
            curr_k = 1
            k = 1
            last = time
            continue
        if (time-last) <= 1000:
            curr_k += 1
            k = max(k,curr_k)
        else:
            curr_k = 1
        last = time
    else:
        curr_k = 0
print(k)