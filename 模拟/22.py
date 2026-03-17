n = int(input())
s = 8100178706957568

chars = "0123456789ABCDEFGHIGKLMNOPQRSTUVWXYZ"
res = []

while n > 0:
    res.append(chars[n % x])
    n //= x
    res = ''.join(res)