#会超时
# w,h = map(int,input().split())
# s = w*h
# ans = 0
# for i in range(2,min(w,h)+1):
#     if w % i == 0 and h % i == 0:
#         t = w//i * h//i
#         ans = max(ans,t)
# print(ans)

import math
w, h = map(int, input().split())
g = math.gcd(w, h)
if g < 2:
    print(0)
else:
    step = 0
    for i in range(2, int(math.isqrt(g)) + 1):
        if g % i == 0:
            step = i
            break
    if step == 0:
        step = g
    ans = (w // step) * (h // step)
    print(ans)