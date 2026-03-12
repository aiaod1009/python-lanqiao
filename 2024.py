# 1 进制转换 + 字符串模拟
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

# 2 模拟
# mod=10**9 + 7
# n = pow(9,10000,mod)
# x = pow(8,10000,mod) #没7或者没3的
# y = pow(7,10000,mod) #又没7又没3的
# print((n-2*x+y)%mod)

#3 模拟，哈希表
# from collections import defaultdict
# n,m = map(int,input().split())
# a=[]
# for i in range(n):
#     a.append(list(map(int, input().split())))
#
# diag1 = defaultdict(lambda: defaultdict(int))
# diag2 = defaultdict(lambda: defaultdict(int))
#
# for i in range(n):
#     for j in range(m):
#         val = a[i][j]
#         diag1[val][i-j] += 1
#         diag2[val][i+j] += 1
# count = 0
# for val in diag1:
#     for n in diag1[val].values():
#         count += n * (n-1)
#     for n in diag2[val].values():
#         count += n * (n-1)
#
# print(count)

# 4
import sys
from datetime import datetime,timedelta
T = int(input())

d0 = datetime(1970,1,1,0,0,0)

for _ in range(T):
    s = sys.stdin.readline().strip()
    part = s.split()
    t = ' '.join(part[:2])
    x = int(part[2])
    t1 = datetime.strptime(t,"%Y-%m-%d %H:%M:%S")
    total = (t1 - d0).total_seconds()
    x *= 60
    last = total - (total % x)

    ans = d0 + timedelta(seconds=last)
    print(ans.strftime("%Y-%m-%d %H:%M:%S"))
















