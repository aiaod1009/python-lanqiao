import sys
lines = [line.strip() for line in sys.stdin]
t = int(lines[0])
idx = 1
for _ in range(t):
    # 去程
    parts1 = lines[idx].split()
    idx += 1
    if len(parts1) == 2:
        dep1, arr1 = parts1
        add1 = 0
    else:
        dep1, arr1, day1 = parts1
        add1 = int(day1[1:-1]) * 86400
                  #这里得到+1/+2,int转化成1/2
    # 回程
    parts2 = lines[idx].split()
    idx += 1
    if len(parts2) == 2:
        dep2, arr2 = parts2
        add2 = 0
    else:
        dep2, arr2, day2 = parts2
        add2 = int(day2[1:-1]) * 86400
    # 转换为秒并计算差值
    h1, m1, s1 = map(int, dep1.split(':'))
    dep_sec1 = h1 * 3600 + m1 * 60 + s1
    h1, m1, s1 = map(int, arr1.split(':'))
    arr_sec1 = h1 * 3600 + m1 * 60 + s1 + add1
    diff1 = arr_sec1 - dep_sec1

    h2, m2, s2 = map(int, dep2.split(':'))
    dep_sec2 = h2 * 3600 + m2 * 60 + s2
    h2, m2, s2 = map(int, arr2.split(':'))
    arr_sec2 = h2 * 3600 + m2 * 60 + s2 + add2
    diff2 = arr_sec2 - dep_sec2

    flight = (diff1 + diff2) // 2
    h = flight // 3600
    m = (flight % 3600) // 60
    s = flight % 60
    print(f"{h:02d}:{m:02d}:{s:02d}")