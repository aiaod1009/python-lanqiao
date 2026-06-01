# n = int(input())
# arr = [input() for _ in range(n)]
# min_total = 999999
# # 总共有 2^n 种组合，循环每一种
# total_case = 2 ** n
# for case in range(total_case):
#     # 先构造当前这一组的字符串
#     now = []
#     temp = case
#     for s in arr:
#         # temp 奇偶判断：0不反转，1反转
#         if temp % 2 == 1:
#             now.append(s[::-1])
#         else:
#             now.append(s)
#         temp = temp // 2  # 看下一位
#     # 计算当前组合的拼接长度
#     res = 2
#     last_char = now[0][1]
#     for i in range(1, n):
#         if now[i][0] == last_char:
#             res += 1
#         else:
#             res += 2
#         last_char = now[i][1]
#     if res < min_total:
#         min_total = res
# print(min_total)

#满分
n=int(input())
a=[]
for i in range(n):
    a.append(input())

#dp[i][j] 前i个，反转为j的最小长度
dp=[[0]*2 for i in range(n)]
dp[0][0],dp[0][1]=2,2
for i in range(1,n):
    for j in range(2): # 当前第i个工件的状态：0=不反转，1=反转
        l0,l1=0,0
        #上一个不反转是否相等
        if a[i-1][1]==a[i][j]:
            l0=1
        # 上一个反转是否相等
        if a[i - 1][0] == a[i][j]:
            l1=1
        dp[i][j]=min(dp[i-1][0]-l0,dp[i-1][1]-l1)+2
print(min(dp[n-1]))