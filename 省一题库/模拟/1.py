import sys
x = [int(sys.stdin.readline().strip()) for i in range(12)]
# print(x)
sheng = 0
cun = 0
for i in range(1,13):
    sheng += 300-x[i-1]
    if sheng>=100:
        cun += sheng-sheng % 100
        sheng %= 100
    if sheng <0:
        print(-i)
        break

if sheng > 0:print(cun*12//10+sheng)

