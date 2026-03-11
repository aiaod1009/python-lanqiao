import sys

n = int(input())
a = list(map(int,sys.stdin.readline().split()))
# 暴力
# count = 0
# for i in range(N):
#     for j in range(i+1,N):
#         if A[i] > A[j]:
#             count += 1
# print(count)


def ms(arr):
    if len(arr) <= 1:
        return arr,0
    m = len(arr) // 2
    L,c1 = ms(arr[:m])
    R,c2 = ms(arr[m:])
    res = []
    i = j = c = 0
    while i < len(L) and j < len(R):
        if L[i] <= R[j]:
            res.append(L[i])
            i += 1
        else:
            res.append(R[j])
            j += 1
            c += len(L) - i
    res += L[i:] + R[j:]
    return res,c1+c2+c
print(ms(a)[1])
