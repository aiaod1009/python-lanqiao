n = int(input())
tot=n
caps = n
while caps >= 3:
    new = caps // 3
    tot += new
    caps = (caps % 3) + new
print(tot)

#公式法
# n = int(input())
# print(n + (n - 1) // 2)