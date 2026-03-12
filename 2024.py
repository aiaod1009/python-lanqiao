# 1进制转换 + 字符串模拟
# def si(n):
#     if n == 0:
#         return '0'
#     res = []
#     while n > 0:
#         res.append(str(n % 4))
#         n = n // 4
#     return ''.join(reversed(res))
#
# count = 0
# for i in range(1,2025):
#     sum1 = sum(int(c) for c in bin(i)[2:])
#     sum2 = sum(int(c) for c in si(i))
#     if sum1 == sum2:
#         count += 1
# print(count)

#2
mod=10**9 + 7
n = pow(9,10000,mod)
x = pow(8,10000,mod) #没7或者没3的
y = pow(7,10000,mod) #又没7又没3的
print((n-2*x+y)%mod)