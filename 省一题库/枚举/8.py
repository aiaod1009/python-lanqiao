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
