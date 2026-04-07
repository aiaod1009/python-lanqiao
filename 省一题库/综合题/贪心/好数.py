n = int(input())
tot = 0
for i in range(1,n+1):
    x = i
    pos=1
    ok = True
    while x > 0:
        d = x % 10
        if pos % 2 == 0 and d % 2 != 0:
            ok = False
            break
        elif pos % 2 == 1 and d % 2 == 0:
            ok = False
            break
        x //= 10
        pos += 1
    if ok:
        tot += 1
print(tot)
        
