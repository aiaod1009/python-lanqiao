n = 1
m = 20230610
h = 1
tot = 1
while tot <= m:
    n += h+1
    tot += n
    h += 1
print(h-1)