ans=0
for n in range(1,1000001):
    sn = sorted(str(n))
    for a in range(1,int(n**0.5)+1):
        if n % a == 0:
            b = n // a
            if sorted(str(a)+str(b)) == sn:
                ans+= 1
                break
print(ans)
