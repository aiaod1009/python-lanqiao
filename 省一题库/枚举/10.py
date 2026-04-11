from datetime import datetime
a,b,c=map(int,input().split('/'))
res=set()
def check(y,m,d):
    try:
        return 1960<=y<=2059 and datetime(y,m,d)
    except:
        return False
# 枚举所有6种格式
for y,m,d in [(1900+a,b,c),(2000+a,b,c),(1900+c,a,b),(2000+c,a,b),(1900+c,b,a),(2000+c,b,a)]:
    if check(y,m,d):
        res.add((y,m,d))
# 排序输出
for y,m,d in sorted(res):
    print(f"{y}-{m:02d}-{d:02d}")





# from datetime import datetime
# a,b,c = (map(int,input().split('/')))
#
# def check(y,m,d):
#     try:
#         return 1960 <= y <= 2059 and datetime(y,m,d)
#     except:
#         return False
#
# res = set()
# # 格式1：年/月/日 → 年可能是 19xx 或 20xx
# # 年 = a → 1900+a 或 2000+a
# if check(1900+a, b, c): res.add((1900+a, b, c))
# if check(2000+a, b, c): res.add((2000+a, b, c))
#
# # 格式2：月/日/年 → 年 = c → 1900+c 或 2000+c
# if check(1900+c, a, b): res.add((1900+c, a, b))
# if check(2000+c, a, b): res.add((2000+c, a, b))
#
# # 格式3：日/月/年 → 年 = c → 1900+c 或 2000+c
# if check(1900+c, b, a): res.add((1900+c, b, a))
# if check(2000+c, b, a): res.add((2000+c, b, a))
#
# for y, m, d in sorted(res):
#     print(f"{y}-{m:02d}-{d:02d}")


