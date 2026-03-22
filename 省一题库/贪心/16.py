a,b,c = map(int,input().split())
#意思是：必须有两个相同或者第二长的是B
if a==b or b==c or a==c or (a<b and b<c) or (c<b and b<a):
    print(0)
else:
    print(min(abs(a - b), abs(b - c), abs(a - c)))