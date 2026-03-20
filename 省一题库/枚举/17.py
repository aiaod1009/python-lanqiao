c = [0] * 4047
for i in range(1,2024):
    c[i] += i

for i in range(1,2024):
    for j in range(i+1,2024):
        c[i + j] += i
print(max(c))