import math
#把元素的所有排列组合都列出来，不重复、不遗漏
from itertools import permutations

n = int(input())
mg, bn = 0, float('inf')

for p in permutations("12345678"):
    s = "".join(p)
    for i in "12345678":  #要插入的数字
        for j in range(9): #要插入的位置
            num = int(s[:j]+i+s[j:])
            g = math.gcd(num, n)
            if g>mg or (g==mg and num<bn):
                mg,bn=g,num
print(bn)