import math
'''
双指针, 用一个指针i表示，表示以i结尾的子数组修改一次后左端最远延伸到j, 
那么以i结尾的子数组左端取任意的j ~ i-1都是满足条件的子数组
'''
n, g = map(int, input().split())
a = [0]+list(map(int, input().split()))

last = 0; res = 0
j = 1
for i in range(1, n+1):
  t = math.gcd(g, a[i])
  if t != g:
    j = last + 1
    last = i
  if i-j+1 >= 2: res += i-j

print(res)