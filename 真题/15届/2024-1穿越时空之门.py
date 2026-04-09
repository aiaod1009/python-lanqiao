# def sijin(n):
#     if n == 0:
#         return '0'
#     res=[]
#     while n > 0:
#       res.append(str(n%4))
#       n = n  // 4
#     return ''.join(reversed(res))
#
# count = 0
# for n in range(1,2025):
#     # er = bin(n)
#     sum1=sum(int(c) for c in bin(n)[2:])
#     # si = sijin(n)
#     sum2=sum(int(c) for c in sijin(n))
#     if sum1 == sum2:
#         count += 1
# print(count)

def jz(x,n):
    ans=0
    while x > 0:
        ans += x%n
        x //= n
    return ans
sum=0
for i in range(1,2025):
    if jz(i,2) == jz(i,4):
        sum += 1
print(sum)