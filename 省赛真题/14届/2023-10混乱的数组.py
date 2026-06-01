n=int(input())
m=n-1
flag=1
k=1
if n==0:
    print(flag)
    print(flag)
else:
    while m - k >= 0:
        m = m - k
        k += 1
        flag += 1
    flag+=1
    m+=2
    ans=[]
    for i in range(1,m):
        ans.append(i)
    for i in range(1,flag+1-m):
        ans.append(i)
    ans.sort(reverse=True)
    ans.insert(0,m)
    print(flag)
    print(" ".join(str(i) for  i in ans))
#
#
#另一种办法 只能过20%
# x = int(input())
#
# # ---------------------- 1. 笨办法找最短长度 L ----------------------
# if x == 0:
#     print(1)
#     print(1)
#     exit()
#
# L = 1
# while L * (L - 1) // 2 < x:
#     L += 1
#
# max_inv = L * (L - 1) // 2  # 长度为L的完全逆序数组最多逆序对
# delta = max_inv - x          # 需要减少的逆序对数量
#
# # ---------------------- 2. 构造字典序最小的数组 ----------------------
# # 思路：从后往前，把最后delta个元素往前挪，减少delta个逆序对
# arr = list(range(L, 0, -1))  # 完全逆序数组 [L, L-1, ..., 1]
# if delta > 0:
#     # 把最后一个元素往前移delta位
#     last = arr.pop()
#     arr.insert(len(arr) - delta, last)
#
# # ---------------------- 3. 输出答案 ----------------------
# print(L)
# print(' '.join(map(str, arr)))