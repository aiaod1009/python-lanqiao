import sys
n = int(sys.stdin.readline().strip())
nodes = [[] for _ in range(n)]

for line in sys.stdin:
    l = line.strip()
    if not l:
        continue
    x = l.split()
    if x[0] == 'add':
        nodes[0].append(x[1])
    elif x[0]== 'sync':
        f_id = int(x[1])
        nodes[f_id].append(nodes[0][len(nodes[f_id])])
    else:
        if n == 1:
            print(0)
        else:
            ml = min(len(nodes[i]) for i in range(1,n))
            print(ml)

