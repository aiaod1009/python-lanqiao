#1
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


#2
with open("words.txt",'r',encoding="UTF-8") as f:
    data = [l.strip() for l in f if l.strip()]
data.sort(key=lambda x:len(x))

bea = set()
ans = ''
for i in data:
    if len(i) == 1 or ''.join(sorted(i[:-1])) in bea:
        bea.add(''.join(sorted(i)))
        if len(i) > len(ans) or (len(i) == len(ans) and i < ans):
            ans = i
print(ans)





















