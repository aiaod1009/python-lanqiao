import os
import sys

# 请在此输入您的代码

s = list('WHERETHEREISAWILLTHEREISAWAY')
n = len(s)

# 冒泡排序
for i in range(n):
    for j in range(n-1-i):
        if ord(s[j]) > ord(s[j+1]):
            s[j], s[j+1] = s[j+1], s[j]

print(''.join(s))  # 输出：AAAAEEEEEEHHIIILLLRRSSTTWWWY

# # 1. 原始字符串
# s = 'WHERETHEREISAWILLTHEREISAWAY'
#
# # 2. 转成列表（因为字符串不可变，sort()是列表的方法）
# s_list = list(s)
#
# # 3. 直接调用sort()，默认按字符的ASCII码升序排列（字母顺序）
# s_list.sort()
#
# # 4. 拼接回字符串输出
# result = ''.join(s_list)
# print(result)