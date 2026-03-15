h,w = map(int,input().split())
d = '2025'*(w+h)

for i in range(h):
    print(d[i:i+w])


#适合数字大的情况，数学取模：
h, w = map(int, input().split())
base = '2025'  # 基础循环串
base_len = len(base)  # 4

for row in range(h):
    # 每行从 row 开始，生成 w 个字符
    line = []
    for col in range(w):
        # 当前位置 = 行偏移 + 列偏移 → 对4取模找对应字符
        idx = (row + col) % base_len
        line.append(base[idx])
    # 拼接成字符串输出
    print(''.join(line))