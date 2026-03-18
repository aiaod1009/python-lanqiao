n = int(input())
jige = 0
youxiu = 0
for i in range(n):
    x = int(input())
    if x >= 60:
        jige += 1
    if x >= 85:
        youxiu += 1
x = round(jige / n *100)
y = round(youxiu / n *100)
print(f"{x}%")
print(f"{y}%")
