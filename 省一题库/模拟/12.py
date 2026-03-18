w,m,n = map(int,input().split())
# l = max(m,n)
# x = []
# d = 1
# for i in range(1,l//w+2):
#     # x.append(list(j for j in range(d,d+w)))
#     if i % 2 == 0:
#         x.append(list(j for j in range(d + w -1,d-1,-1)))
#     else:
#         x.append(list(j for j in range(d, d + w)))
#     d = d+w
# print(x)
# l1,l2,w1,w2 = 0,0,0,0
# for i in range(l//w+1):
#     for j in range(w):
#         if x[i][j] == m:
#             l1 = i
#             w1 = j
#         if x[i][j] == n:
#             l2 = i
#             w2 = j
def pos(num):
    if num % w == 0:
        row = num // w
        col = w
    else:
        row = num // w + 1
        col = num % w
    if row % 2 == 0:
        col = w + 1 - col  #奇偶反转核心公式
    return row,col
l1,w1 = pos(m)
l2,w2 = pos(n)

print(abs(l2-l1)+abs(w1-w2))