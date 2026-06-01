s = input()

count = {}
for i in s:
    if i in count:
        count[i] += 1
    else:
        count[i] = 1

m1 = ''
m2 = 0

for c in sorted(count.keys()):
    if count[c] > m2:
        m2 = count[c]
        m1 = c

print(m1)
print(m2)
