n = int(input().strip())
a = sorted(list(map(int,input().split())))
b = sorted(list(map(int,input().split())))
# c = [a[i]-b[i] for i in range(n)]
res = 0
i = n-1
j = n-1
while i >= 0 and j >= 0:
    if b[j] < a[i]:
        i -= 1
        j -= 1
    else:
        res += 1
        j -= 1
print(res)