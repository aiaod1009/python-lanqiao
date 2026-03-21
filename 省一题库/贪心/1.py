n = input().strip()
if sum(int(c) for c in n) == 1:
    print(n)
else:
    print('1'+'0' * len(n))

#其他方法
a=int(input())
b=1
while b<a:
   b*=10
print(b)
