import sys
input = lambda:sys.stdin.readline().strip()
m = int(input())
w = []
for i in range(m):
    op,l = map(int,input().split())
    if op == 1:
        if l in w:
            print("Already Exist")
        else:
            w.append(l)
    else:
        if not w:
            print("Empty")
            continue
        best = w[0]
        for x in w:
            if abs(x-l) < abs(best-l):
                best = x
            elif abs(x-l)==abs(best-l) and x<best:
                best = x
        print(best)
        w.remove(best)


# 二分
import bisect
w = []
m = int(input())
for _ in range(m):
    op, l = map(int, input().split())
    if op == 1:
        # 进货：二分查有没有，没有就插入（保持有序）
        idx = bisect.bisect_left(w, l)
        if idx < len(w) and w[idx] == l:
            print("Already Exist")
        else:
            bisect.insort(w, l)
    else:
        # 出货：二分找位置
        if not w:
            print("Empty")
            continue
        idx = bisect.bisect_left(w, l)
        best = 0
        # 情况1：所有木头都比 l 大 → 拿第一个
        if idx == 0:
            best = w[0]
        # 情况2：所有木头都比 l 小 → 拿最后一个
        elif idx == len(w):
            best = w[-1]
        # 情况3：左右都有，选更近的；一样近选小的
        else:
            left = w[idx - 1]
            right = w[idx]
            if l - left <= right - l:
                best = left
            else:
                best = right
        w.remove(best)
        print(best)