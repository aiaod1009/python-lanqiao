#1 暴力枚举
# def find_i(i):
#     a = i.find('2')
#     if a == -1:
#         return 0
#     b = i.find('0',a+1)
#     if b == -1:
#         return 0
#     c = i.find('2', b + 1)
#     if c == -1:
#         return 0
#     d = i.find('3', c + 1)
#     if d == -1:
#         return 0
#     return 1
# cnt = 0
# for i in range(12345678,98765433):
#     if find_i(str(i)) == 0:
#         cnt += 1
# print(cnt)

# 2 枚举
max_cnt = [0] * 4046
for i in range(1,2023):
    max_cnt[i] += i

for i in range(1,2023):
    for j in range(i+1,2023):
        s = i + j
        add = min(i,j)
        max_cnt[s] += add
print(max(max_cnt))

















