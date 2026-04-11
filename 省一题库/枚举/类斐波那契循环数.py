def pd(x):
    s=str(x)
    n=len(s)
    a=[]
    for i in range(n):
        a.append(int(s[i]))
    b=a
    while 1==1:
        t=0
        for i in range(len(b)-n,len(b)):
            t+=b[i]
        if t>10000000 :
            return 0
        if t==x:
            return 1
        b.append(t)


for i in range(10000000, 0, -1):
    if pd(i) == 1:
        print(i)
        break
print(7913837)


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

