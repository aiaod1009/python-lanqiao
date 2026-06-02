cnt = 0
for i in range(1,2021):
    for c in str(i):
        if c == '2':
            cnt += 1
            break
print(cnt)

# 一行版:print(sum(1 for i in range(1,2021) if '2' in str(i)))