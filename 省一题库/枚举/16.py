cnt = 0
for n in range(1,1000001):
    for a in range(1,int(n**0.5)+1):
        if n % a == 0:
            b = n // a
            sa,sb = str(a),str(b)
            sab = sa + sb
            sn = str(n)
            if sorted(sab) == sorted(sn):
                cnt += 1
                break
print(cnt)

