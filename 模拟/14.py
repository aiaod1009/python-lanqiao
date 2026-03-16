# n = int(input())
# t = ['jia', 'yi', 'bing', 'ding', 'wu', 'ji', 'geng', 'xin', 'ren', 'gui']
# d = ['zi', 'chou', 'yin', 'mao', 'chen', 'si', 'wu', 'wei', 'shen', 'you', 'xu', 'hai']
# tian = (n-4)%10
# di = (n-4)%12
# print(f"{t[tian]}{d[di]}")


# n = int(input())
#
# # 题目给的锚点：2020年 = 庚子年
# base_year = 2020
# base_tian = 6  # "geng" 在天干列表里的索引
# base_di = 0    # "zi" 在地支列表里的索引
#
# # 拼音列表（顺序是固定的，题目样例也能反推）
# tian = ["jia", "yi", "bing", "ding", "wu", "ji", "geng", "xin", "ren", "gui"]
# di   = ["zi", "chou", "yin", "mao", "chen", "si", "wu", "wei", "shen", "you", "xu", "hai"]
#
# diff = n - base_year
# tian_idx = (base_tian + diff) % 10
# di_idx = (base_di + diff) % 12
#
# print(tian[tian_idx] + di[di_idx])

n = int(input())

# 天干列表：索引0=庚（对应2020年），按顺序往后排
tian = ["geng", "xin", "ren", "gui", "jia", "yi", "bing", "ding", "wu", "ji"]
# 地支列表：索引0=子（对应2020年），按顺序往后排
di = ["zi", "chou", "yin", "mao", "chen", "si", "wu", "wei", "shen", "you", "xu", "hai"]

# 计算偏移量（2020年对应偏移量0）
offset = n - 2020
# 取模保证循环
t_idx = offset % 10
d_idx = offset % 12

print(tian[t_idx] + di[d_idx])