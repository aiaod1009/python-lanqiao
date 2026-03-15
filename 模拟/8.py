h,w = map(int,input().split())
d = '2025'*(w+h)

for i in range(h):
    print(d[i:i+w])