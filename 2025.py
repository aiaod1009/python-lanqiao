#1模拟
# n = 2025
# s = 0
# while n > 0:
#     if s % 2 == 0:
#         n -= (5+2)
#         if s % 3 == 1:
#             n -= 2
#         elif s % 3 == 2:
#             n -= 10
#         else:
#             n -= 7
#     else:
#         n -= (5+15)
#         if s % 3 == 1:
#             n -= 2
#         elif s % 3 == 2:
#             n -= 10
#         else:
#             n -= 7
#     s += 1
# print(s)


#2字符串模拟+状态dp
# with open("words.txt",'r',encoding="UTF-8") as f:
#     data = [l.strip() for l in f if l.strip()]
# data.sort(key=lambda x:len(x))
#
# bea = set()
# ans = ''
# for i in data:
#     if len(i) == 1 or ''.join(sorted(i[:-1])) in bea:
#         bea.add(''.join(sorted(i)))
#         if len(i) > len(ans) or (len(i) == len(ans) and i < ans):
#             ans = i
# print(ans)



3模拟
w,h,v = map(int,input().split())
for i  in range(h + w):
    if i < h:
        print(''.join('Q' for _ in range(w)))
    else:
        print(''.join('Q' for _ in range(w+v)))

for i in range(h):
    print("Q" * w)
for i in range(w):
    print("Q" * (w+v))























