import math
def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

cnt = 0
max_n = 20210605
for num in range(2, max_n+1):
    # 检查每一位只能是2/3/5/7
    s = str(num)
    flag = True # 标记「数字每一位是否全是 2/3/5/7」
    for c in s:
        if c not in {'2','3','5','7'}:
            flag = False
            break
    if not flag:# flag == False:
        continue # 不再判断这个数是不是质数，去遍历下一个 num
    if is_prime(num):
        cnt += 1
print(cnt)