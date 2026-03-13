#1 2023  暴力枚举 f
def find_i(i):
    a = i.find('2')
    if a == -1:
        return 0
    b = i.find('0',a+1)
    if b == -1:
        return 0
    c = i.find('2', b + 1)
    if c == -1:
        return 0
    d = i.find('3', c + 1)
    if d == -1:
        return 0
    return 1
cnt = 0
for i in range(12345678,98765433):
    if find_i(str(i)) == 0:
        cnt += 1
print(cnt)