import sys

m = []
for _ in range(300):
    line = sys.stdin.readline().strip()
    m.append(line)

count = 0
for i in range(300):
    for j in range(297):
        if m[i][j:j+4] == '2020':
            count += 1


for j in range(300):
    for i in range(297):
        if (m[i][j] == '2' and
            m[i+1][j] == '0' and
            m[i+2][j] == '2' and
            m[i+3][j] == '0'):
            count += 1

for i in range(297):
    for j in range(297):
        if (m[i][j] == '2' and
            m[i+1][j+1] == '0' and
            m[i+2][j+2] == '2' and
            m[i+3][j+3] == '0'):
            count += 1
print(count)
