# Kadane 算法
n,k = map(int,input().split())
a = list(map(int,input().split()))
tot = sum(a)

if k == 1:
    print(tot)
else:
    m = curr = a[0]
    for num in a[1:]:
        curr = max(num,curr+num) #以当前数字结尾的最大连续子段和
        m = max(m,curr)  #遍历到目前为止，全局最大的连续子段和
    print(tot + (k-1)*m)