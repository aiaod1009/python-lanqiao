import math
def p(x):
    if x < 2:
        return False
    for i in range(2,int(math.isqrt(x))+1):
        if x % i == 0:
            return False
    return True

def dfs(i,num,s):
    if i == len(s):
        return num if p(num) else -1
    if s[i] != '*':
        return dfs(i+1,num*10+int(s[i]),s)
    for d in range(10):
        res = dfs(i+1,num*10+d,s)
        if res != -1:
            return res
    return -1
t = int(input())
for _ in range(t):
    s = input().strip()
    print(dfs(0,0,s))
