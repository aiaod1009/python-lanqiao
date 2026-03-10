n = 2025
s = 0
while n > 0:
    if s % 2 == 0:
        n -= (5+2)
        if s % 3 == 1:
            n -= 2
        elif s % 3 == 2:
            n -= 10
        else:
            n -= 7
    else:
        n -= (5+15)
        if s % 3 == 1:
            n -= 2
        elif s % 3 == 2:
            n -= 10
        else:
            n -= 7
    s += 1
print(s)
