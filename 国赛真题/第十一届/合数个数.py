import math
cnt = 0
for i in range(2,2021):
    f = True
    for j in range(2,math.isqrt(i)+1):
        if i % j == 0:
            f = False
    if f:cnt += 1
print(2020-cnt-1)