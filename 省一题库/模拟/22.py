s = 8100178706957568
chars = "0123456789ABCDEFGHIGKLMNOPQRSTUVWXYZ"
for i in range(11,37):
    n = s
    res = []
    while n > 0:
        res.append(chars[n % i])
        n //= i
    x = ''.join(res)
    if x.isdigit():
        print(i)
        break