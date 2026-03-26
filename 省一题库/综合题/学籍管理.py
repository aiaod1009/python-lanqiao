import sys
input = lambda:sys.stdin.readline().strip()
d = {}
q = int(input())
for _ in range(q):
    s = input().split()
    op = int(s[0])
    if op == 1:
        d[s[1]] = s[2]
        print("OK")
    elif op == 2:
        if s[1] in d:
            print(d[s[1]])
        else:
            print("Not found")
    elif op == 3:
        if s[1] in d:
            del d[s[1]]
            print("Deleted successfully")
        else:
            print("Not found")
    else:
        print(len(d))