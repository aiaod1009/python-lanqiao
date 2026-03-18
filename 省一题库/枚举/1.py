def zhi(n):
    if n < 2:
        return False
    for i in range(2,int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
a = []
i = 2
while len(a) < 2025:
    if zhi(i):
        a.append(i)
    i += 1
print(a[2024])