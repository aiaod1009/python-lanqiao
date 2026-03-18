ans=0
for d in range(1,2025//2+1):
    num=2025-2*d
    ans+=num*2
print(ans)


#数学组合数方法
odd = 1013
even = 1012

c_odd = odd * (odd - 1) // 2
c_even = even * (even - 1) // 2

total = 2 * (c_odd + c_even)
print(total)