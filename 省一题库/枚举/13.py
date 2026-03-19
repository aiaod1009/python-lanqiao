for x in range(9999999, 0, -1):
    d = [int(c) for c in str(x)]
    n = len(d)
    s = d.copy()
    for _ in range(1000):
        t = sum(s[-n:])
        if t == x:
            print(x)
            exit()
        if t > x:
            break
        s.append(t)
print(0)