n = int(input().strip())
res = ['']*n
def dfs(pos):
    if pos == n:
        print(''.join(res))
        return
    res[pos] = 'N'
    dfs(pos+1)
    res[pos] = 'Y'
    dfs(pos+1)

dfs(0)

#n位二进制数
n = int(input())
# 总共有 2^n 种情况
for i in range(1 << n):  #核心作用是计算2的n次方
    # 把数字转成二进制字符串，补零到n位，然后替换字符
    # bin(i) 把数字转成二进制字符串时，Python 会自动加 0b 前缀（0b 是二进制的标识）
    s = bin(i)[2:].zfill(n) #给字符串左侧补 0
    s = s.replace('0', 'N').replace('1', 'Y')
    print(s)





