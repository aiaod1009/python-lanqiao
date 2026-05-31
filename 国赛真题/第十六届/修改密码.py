import sys
input = lambda:sys.stdin.readline().strip()
n= int(input().strip())
for _ in range(n):
    s = input()
    types = set()
    for c in s:
        # types = {'1' if c.islower() else "2" if c.isupper() else "D" }
        if c.islower():
            types.add('1')  # 小写字母贴 '1'
        elif c.isupper():
            types.add('2')  # 大写字母贴 '2'
        else:
            types.add('3')
    m = 3 - len(types)
    mc = sum(1 for c in s if c in 'Oo0')
    if m == 0:
        print(0)
    elif mc < m:
        print(-1)
    else:
        print(m)



#繁琐代码
# import sys
# # 读取账号数量 n
# n = int(sys.stdin.readline().strip())
# # 循环处理每个密码
# for _ in range(n):
#     s = sys.stdin.readline().strip()
#     # 1. 检查原密码自带哪些元素
#     has_lower = False
#     has_upper = False
#     has_digit = False
#     # 2. 统计手里“魔法字符”的总数
#     magic_count = 0
#     for char in s:
#         if char.islower():
#             has_lower = True
#         if char.isupper():
#             has_upper = True
#         if char.isdigit():
#             has_digit = True
#         # 如果是 O, o, 0 中的任何一个，魔法储备 +1
#         if char in ('O', 'o', '0'):
#             magic_count += 1
#     # 3. 计算一共缺了几种类型
#     missing_types = 0
#     if not has_lower: missing_types += 1
#     if not has_upper: missing_types += 1
#     if not has_digit: missing_types += 1
#     # 4. 根据我们的分类讨论，直接得出答案
#     if missing_types == 0:
#         print(0)
#     elif magic_count < missing_types:
#         # 魔法字符不够补窟窿（包括 magic_count == 0 的情况）
#         print(-1)
#     else:
#         # 魔法字符够用，缺几个窟窿，最少就需要变几次
#         print(missing_types)