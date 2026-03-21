n = int(input())
a = [0]+list(map(int,input().split()))
res = 0
for i in range(1,n+1):
    while a[i] != i:
        tmp = a[a[i]]
        a[a[i]] = a[i]
        a[i] = tmp
        res += 1
print(res)

# 暴力
# n = int(input())
# a = list(map(int, input().split()))
# ans = 0
# for i in range(n):
#     for j in range(n):
#         ans += (a[i] ^ a[j]) * abs(i - j)
# print(ans)


# def ms(arr):
#     if len(arr) <= 1:
#         return arr,0
#     m = len(arr) // 2
#     L,c1 = ms(arr[:m])
#     R,c2 = ms(arr[m:])
#     res = []
#     i = j = c = 0
#     while i < len(L) and j < len(R):
#         if L[i] <= R[j]:
#             res.append(L[i])
#             i += 1
#         else:
#             res.append(R[j])
#             j += 1
#             c += len(L) - i
#     res += L[i:] + R[j:]
#     return res,c1+c2+c
# print(ms(a)[1])
