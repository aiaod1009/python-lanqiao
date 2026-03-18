n = int(input())
x = int(input())

chars = "0123456789ABCDEFGHIGKLMNOPQRSTUVWXYZ"
res = []

while n > 0:
    res.append(chars[n % x])
    n //= x
res.reverse()
print(''.join(res))