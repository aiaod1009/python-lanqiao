import os
import sys

# python是这样的，只要写就可以了，其他语言要考虑的就很多了
def fun(s):
  for i in range(len(s),-1,-1):
    if s[0:i//2]==s[i-1:(i-1)//2:-1]:
      return i

s=input()
ss=s[::-1]
i=0
while i<len(s) and s[i]==ss[i]:
  i+=1
print(2*i+max(fun(s[i:]),fun(ss[i:])))