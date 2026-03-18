def sijin(n):
    if n == 0:
        return '0'
    res=[]
    while n > 0:
      res.append(str(n%4))
      n = n  // 4
    return ''.join(reversed(res))

count = 0
for n in range(1,2025):
    # er = bin(n)
    sum1=sum(int(c) for c in bin(n)[2:])
    # si = sijin(n)
    sum2=sum(int(c) for c in sijin(n))
    if sum1 == sum2:
        count += 1
print(count)