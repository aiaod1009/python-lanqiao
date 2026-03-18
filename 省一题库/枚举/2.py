n = int(input())
total = 0
for i in range(1,n+1):
    s = str(i)
    if '2' in s or '0' in s or '1' in s or '9' in s:
        total += i
print(total)


# 或者
# n = int(input())
# total = 0
# for i in range(1, n+1):
#     flag = False  # 标记是否有符合条件的数位
#     for c in str(i):
#         if c in {'2','0','1','9'}:
#             flag = True
#             break  # 找到一个就可以跳出内层循环了
#     if flag:
#         total += i
# print(total)