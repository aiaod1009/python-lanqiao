# 1	排列字母	字符串、排序 / 模拟	⭐⭐	基础字符串处理，按规则排序 / 拼接
# s = 'WHERETHEREISAWILLTHEREISAWAY'
# s = sorted(s)
# print(''.join(s))

# 2	寻找整数	数学、枚举 / 打表	⭐⭐⭐	找满足条件的整数，需要数学推导或预处理
#背一下模板，找步长的.如果两个数都满足同一组同余条件，那么它们的差值就是「满足这组条件的解的周期（步长）」
# L=[]
# for i in range(187,10**12,187):
#     if i%44==33 and i%45==29 and i%46==15 and i%47==5 and i%48==41 and i%49==46:
#         L.append(i)
#     if len(L)>=2:
#         break
# print(L)
L=[5458460249, 12590206409]
step=L[1]-L[0]
flag=0
for i in range(L[0],10**17,step):
    if i%20==9 and i%25==9 and i%26==23 and i%27==20 and i%28==25 and i%29==16 and i%30==29 and i%31==27 and i%32==25 and i%33==11 and i%34==17 and i%35==4 and i%36==29 and i%37==22 and i%38==37 and i%39==23 and i%40==9 and i%41==1 and i%42==11 and i%43==11 :
        print(i)
        break

# 3	纸张尺寸	模拟、递推	⭐⭐	模拟纸张对折 / 尺寸变化，简单递推
# n = int(input()[1:])
# l = 1189
# w = 841
# for i in range(n):
#     l , w = w , l // 2
# print(l)
# print(w)

# 4	数位排序	排序、数位和	⭐⭐	自定义排序规则（按数位和排序）
# n = int(input())
# m = int(input())
# a = list(range(1,n+1))
# a.sort(key=lambda x:(sum(int(c) for c in str(x)),x))
# print(a[m-1])


# 5	蜂巢	几何、坐标 / 模拟	⭐⭐⭐⭐	六边形网格坐标与距离计算，偏竞赛思维






# 6	消除游戏	模拟、并查集	⭐⭐⭐⭐
# 7	全排列的价值	数学、排列组合\递推	⭐⭐⭐⭐⭐	高阶数学 / DP，计算排列的贡献和，难度很高
# 8	技能升级	二分	⭐⭐⭐⭐	经典二分 / 优先队列，优化选择问题







# 9	最长不下降子序列	动态规划（LIS）	⭐⭐⭐⭐⭐
# 10	最优清零方案	线段树	⭐⭐⭐⭐⭐	压轴难题，需要贪心 + 数学推导，
import sys; readline = sys.stdin.readline
read = lambda: [int(x) for x in readline().split()]

N, K = read()
arr = [0] + read()

i = 1
ans = 0
while i <= N:
    if i + K - 1 <= N:
        minv = min(arr[i:i+K])
        if minv != 0:
            ans += minv
            for t in range(i, i+K): arr[t] -= minv
        for t in range(i, i+K): # 关键优化
            if arr[t] == 0: i = t
    i += 1
ans += sum(arr)
print(ans)

