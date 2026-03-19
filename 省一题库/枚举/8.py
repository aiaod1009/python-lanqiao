N = int(input())
l = list(map(int,input().split()))
ans = 0  #记录所有起始位置中能获得的最大球票数
for i in range(N):
    pk = 0 #赢得的球票张数
    cnt = 1  #计数器
    l1=l.copy() # 复制原列表，避免修改原始数据
    while l1 and cnt <= max(l1):  #l1不为空而且当前计数器数字不大于l1里面最大的
        if l1[i] == cnt:
            pk += l1.pop(i) # 根据索引移除元素，并返回被移除的元素值
            cnt = 1        # 收集后，计数重置为1
            if len(l1) == 0:
                break    # 无卡片时直接终止
            i = i % len(l1)  # 下一次从【被移除卡片的下一张】开始
        else:
            cnt += 1   # 不匹配，计数+1
            i = (i + 1) % len(l1)   # 索引指向下一张卡片
    if pk > ans:
        ans = pk
print(ans)











# num = int(input())  # 卡片数目
# arr = input()  # 顺时针排列的卡片
# result = 0  # 最后赢的球票张数
# for i in range(num):  # 用 i 的变化来表示从哪里开始数
#     pocket = 0  # 赢来的球票数目
#     nums = 1  # 计数器初始化
#     numarr = list(map(int, arr.split()))  # 初始化 arr 列表于 int 类型
#     while numarr and nums <= max(numarr):  # 循环条件： numarr 列表中还有卡片，且 nums 的数字不大于 numarr 中最大的数字
#         if numarr[i] == nums:  # 满足获取条件时
#             pocket += numarr.pop(i)  # pop()用于删除并返回列表中的一个元素
#             nums = 1  # 计数器重置
#             if len(numarr) == 0:  # 判断 numarr 是否为空
#                 break
#             i = i % len(numarr)  # 循环队列头尾
#         else:  # 不满足获取条件
#             nums += 1
#             i = (i + 1) % len(numarr)  # 循环队列头尾
#     if pocket > result:  # 只要每次循环中赢得球票数量最多的那次结果
#         result = pocket
# print(result)