import os
import sys

# 请在此输入您的代码
T = int(input())
for _ in range(T):
    b1, b2, b3 = map(int, input().split())
    cnta, cntb = map(int, input().split())
    va, vb = map(int, input().split())

    max_total = 0
    # 枚举所有可能的 A 的数量 a
    for a in range(0, cnta + 1):
        a_vol = a * va
        if a_vol > b1 + b2 + b3:
            continue

        # 枚举 A 在三个背包中的所有分配方式 (a1, a2, a3)
        best_b = 0
        for a1 in range(0, min(a, b1 // va) + 1):
            for a2 in range(0, min(a - a1, b2 // va) + 1):
                a3 = a - a1 - a2
                if a3 < 0 or a3 * va > b3:
                    continue

                # 计算剩余空间
                rem1 = b1 - a1 * va
                rem2 = b2 - a2 * va
                rem3 = b3 - a3 * va

                # 计算能装的 B 数量
                b = (rem1 // vb) + (rem2 // vb) + (rem3 // vb)
                b = min(b, cntb)

                if a + b > max_total:
                    max_total = a + b

    print(max_total)

#
# for _ in range(int(input())):
#     B1, B2, B3 = map(int, input().split())
#     cntA, cntB = map(int, input().split())
#     vA, vB = map(int, input().split())
#     if vA > vB:  # 确保积木A的体积比B的体积小
#         cntA, cntB = cntB, cntA
#         vA, vB = vB, vA
#     ans = 0
#     for i in range(cntA + 1):
#         if i * vA > B1:
#             break
#         for j in range(cntA - i + 1):
#             if j * vA > B2:
#                 break
#
#             res = i + j  # res存已经放了多少积木数
#             remainCntA = cntA - i - j
#             remainCntB = cntB
#             remain_B1 = B1 - vA * i
#             remain_B2 = B2 - vA * j
#             remain_B3 = B3
#
#             # 将B放入背包1和背包2中
#             res += min(remain_B1 // vB, cntB)  # 将背包1的剩余空间用B积木尽量装
#             remainCntB -= min(remain_B1 // vB, remainCntB)
#             res += min(remain_B2 // vB, remainCntB)
#             remainCntB -= min(remain_B2 // vB, remainCntB)
#
#             # 剩下的背包3先用余下的A装
#             res += min(remain_B3 // vA, remainCntA)
#             remain_B3 -= min(remain_B3 // vA, remainCntA) * vA
#             # 再用B补充余下的背包空间
#             res += min(remain_B3 // vB, remainCntB)
#
#             ans = max(ans, res)
#     print(ans)