cnt = 0
for i in range(1,2021):
    for c in str(i):
        if c == '2':
            cnt += 1
            break
print(cnt)